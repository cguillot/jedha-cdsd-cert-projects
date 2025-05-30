import logging
import streamlit as st
from streamlit import session_state as state
from PIL import Image
from predictors import available_models
import time
import os

logging.info('Starting traffic signs models demo...')
print('print: Starting traffic signs models demo...')

### Config
st.set_page_config(
    page_title="Traffic Signs models tester",
    page_icon="\U0001F6A6",
    layout="wide",
    initial_sidebar_state="expanded"
)

### App
st.title("Traffic Signs models tester")


# Initialize some states
if "assess_all_models" not in st.session_state:
    st.session_state.assess_all_models = True

if "prediction_rendered" not in st.session_state:
    st.session_state.prediction_rendered = False

if "images_inference_results" not in st.session_state:
    st.session_state.images_inference_results = []

if "selected_media" not in st.session_state:
    st.session_state.selected_media = None
    st.session_state.selected_media_changed = False

# sidebar
models = available_models()

model_names = [m.get_name() for m in models]
all_models_dict = dict(zip(model_names, models))

st.sidebar.header("Model")
st.sidebar.checkbox('Test all models', key='assess_all_models')

model_option = st.sidebar.selectbox(
    "Select the model you would you like to assess:",
    model_names,
    index=None,
    placeholder="Select a model...",
    disabled=st.session_state.assess_all_models
)

st.sidebar.header("Images & Videos")
st.sidebar.markdown("""
    Upload some pictures and video to assess models on:
""")

st.sidebar.file_uploader(
    "Media uploader",
    type=['jpg', 'png', 'jpeg'],
    accept_multiple_files=True,
    label_visibility="collapsed",
    help="Upload image(s) to predict on. Supported file types: jpg, png, jpeg",
    key="uploaded_imgs",
)

state.file_names = [each_file.name for each_file in state.uploaded_imgs]

# Main area
st.markdown(f"Selected model: **{model_option}**")

## Image selector area
image_selector_col, preview_col = st.columns(2)

preview_image_container = preview_col.container()

st.divider()

#if st.session_state.prediction_rendered == False:
result_container = st.container()


# Get the directory of the current Python file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the directory containing your images relative to the script location
image_dir = os.path.join(script_dir, "demo-images")

# Get the list of image files
local_image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

print('local_image_files: ', local_image_files)

media_names = [img.name for img in state.uploaded_imgs]
media_names_path = [img for img in state.uploaded_imgs]

# Adding local files
# Load the selected image
for image_file in local_image_files:
    image_path = os.path.join(image_dir, image_file)

    media_names.append(image_file)
    media_names_path.append(image_path)

all_medias_dict = dict(zip(media_names, media_names_path))

def is_image(media_name):
    if media_name is None:
        return False
    return media_name.endswith('.jpg') or media_name.endswith('.png') or media_name.endswith('.jpeg')

def is_video(media_name):
    if media_name is None:
        return False
    return media_name.endswith('.mp4') or media_name.endswith('.avi')

def display_media_dashboard():
    selected_media = st.session_state.selected_media
    print(f'Media selected: {selected_media}')
    if selected_media is None:
        return

    if is_image(selected_media):
        image_path = None
        if selected_media in all_medias_dict and not st.session_state.prediction_rendered:
            image_path = all_medias_dict[selected_media]
            image = Image.open(image_path)
            preview_image_container.image(image, use_container_width=True)

def media_selected_changed():
    print('media_selected_changed')
    st.session_state.prediction_rendered = False
    st.session_state.images_inference_results = []

media_option = image_selector_col.selectbox(
    "Select the media to infer on:",
    media_names,
    index=None,
    placeholder="Select a media...",
    on_change=media_selected_changed,
    key="selected_media"
)

def infer_on_media():
    # check we have a model
    if st.session_state.assess_all_models == False and model_option not in all_models_dict:
        st.warning('Please select a model first!')
        return

    # Reset stored results in order to clear display and avoid duplicates
    st.session_state.images_inference_results = []

    with st.spinner("Running..."):
        print(f'inferring in progress...{model_option}')

        inferrable_models = None

        if st.session_state.assess_all_models is False:
            if model_option in all_models_dict:
                inferrable_models = [all_models_dict[model_option]]
        else:
            inferrable_models = [m for (_, m) in all_models_dict.items()]

        for model in inferrable_models:
            selected_media = st.session_state.selected_media

            if is_image(selected_media):
                image_path = None
                if selected_media in all_medias_dict:
                    image_path = all_medias_dict[selected_media]
                    image = Image.open(image_path)
                    result = model.predict(image)

                    result['model_name'] = model.get_name()

                    st.session_state.images_inference_results.append(result)

    st.session_state.prediction_rendered = True

result_cols = result_container.columns(2)
if len(st.session_state.images_inference_results) > 0:
    with result_container:
        result_cols[0].markdown('Detected items')
        result_cols[1].markdown('Details')

        for inference_result in st.session_state.images_inference_results:
            result_cols = st.columns(2)
            attributes_keys = [k for k in inference_result.keys() if k != 'image']
            print('result: ', [inference_result[k] for k in attributes_keys])

            result_cols[1].markdown(f"Model: **{inference_result['model_name']}**")
            result_cols[0].image(inference_result['image'])

            time_to_predict_ms = inference_result['stats']['time_to_predict_ms']

            result_cols[1].markdown(f"""
                                    **inference time**: {time_to_predict_ms:.2f}ms
                                    """)

            if 'detections' in inference_result and len(inference_result['detections']) > 0:
                detections = inference_result['detections']
                print('detections: ', detections)

                labels = "\n".join(f"- {d['label_name']} (conf: {d['confidence']:.2f})" for d in detections)

                result_cols[1].markdown(f"""
                                    **Detected**
                                    {labels}
                                    """)
            else:
                result_cols[1].markdown("""
                                    **nothing detected**
                                    """)

images_count = 0
video_count = 0

for file in media_names:
    if type(file) is str:
        images_count += 1
    elif file.name.endswith('.jpg'):
        images_count += 1

image_selector_col.markdown(f"Medias provided: {images_count} images and {video_count} video")
image_selector_col.button('detect...', on_click=infer_on_media, args=[])

inferred_image_col, predictive_model_stats = st.columns(2)

display_media_dashboard()
