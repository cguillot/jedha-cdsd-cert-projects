import os
import logging

from pathlib import Path

from dotenv import dotenv_values

import typer

from hfdm import (
    HuggingFaceSpaceDeployment,
    HuggingFaceAccount,
)

# secrets
__env = {
    **dotenv_values("../../../.env")
}

app = typer.Typer(no_args_is_help=True)

def get_huggingface_account():
    hf_token = __env["CDSD_HUGGINGFACE_TOKEN"]
    hf_namespace = __env["CDSD_HUGGINGFACE_NAMESPACE"]

    hf = HuggingFaceAccount(hf_namespace, hf_token)

    return hf

def load_huggingface_deployment(deployment_path):
    dep = HuggingFaceSpaceDeployment(deployment_path)

    return dep

@app.command("install")
def cli_deploy_infra(force: bool = False):
    """Deploy infrastructure

    Args:
        force (bool, optional):  Force HuggingFace vars en secrets reset when existing. Defaults to False.
    """
    print("Install or update infra...")

    # Get script's directory
    script_dir = Path(__file__).resolve().parent

    hf_account = get_huggingface_account()

    # Dashboard
    dashboard_deploy_path = script_dir / "uber-hot-zones/hf-deploy.yml"
    dashboard_dep = load_huggingface_deployment(dashboard_deploy_path)

    hf_account.install(dashboard_dep, providers = [], force=force)

    print("Done")

@app.command("destroy")
def cli_destroy_infra():
    """Destroy deployed resources related to the deployment
    """
    print("Destroy infra...")

    # Get script's directory
    script_dir = Path(__file__).resolve().parent

    hf_account = get_huggingface_account()

    dashboard_deploy_path = script_dir / "uber-hot-zones/hf-deploy.yml"
    dep = load_huggingface_deployment(dashboard_deploy_path)
    hf_account.destroy(dep)

    print("Done")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    app()
