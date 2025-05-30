# Provide the custom models

Copy `model1.h5` and `model2.h5` to `.\src\model-tester\models\custom_models`.

# Build docker image

```
docker build . -t model-tester
```

# Run streamlit server

```
docker run --rm -p 7860:7860 model-tester
```
Then, go to http://localhost:7860/
