import os
import logging

from enum import Enum

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

class InstallPackage(str, Enum):
    all = "all"
    api = "api"
    dashboard = "dashboard"

@app.command("install")
def cli_deploy_infra(package: InstallPackage, force: bool = False):
    """Deploy infrastructure

    Args:
        package: un choix parmi [all, api, dashboard]
        force (bool, optional):  Force HuggingFace vars en secrets reset when existing. Defaults to False.
    """
    print("Install or update infra...")

    # Get script's directory
    script_dir = Path(__file__).resolve().parent

    install_api = False
    install_dashboard = False

    match package:
        case InstallPackage.all:
            install_api = True
            install_dashboard = True
        case InstallPackage.api:
            install_api = True
        case InstallPackage.all | InstallPackage.dashboard:
            install_dashboard = True

    hf_account = get_huggingface_account()

    # API
    api_deploy_path = script_dir / "api/hf-deploy.yml"
    api_dep = load_huggingface_deployment(api_deploy_path)

    # Dashboard
    dashboard_deploy_path = script_dir / "dashboard/hf-deploy.yml"
    dashboard_dep = load_huggingface_deployment(dashboard_deploy_path)

    if install_api:
        hf_account.install(api_dep, providers = [], force=force)

    if install_dashboard:
        api_hf_base_url = f"https://{hf_account.namespace}-{api_dep.get_deployment_name()}.hf.space".lower()
        os.environ["CDSD_B5_GETAROUND_PREDICT_API_ENDPOINT_URL"] = f"{api_hf_base_url}/predict"

        hf_account.install(dashboard_dep, providers = [], force=force)

    print("Done")

@app.command("destroy")
def cli_destroy_infra(package: InstallPackage):
    """Destroy deployed resources related to the deployment
    Args:
        package: un choix parmi [all, api, dashboard]
    """
    print("Destroy infra...")

    # Get script's directory
    script_dir = Path(__file__).resolve().parent

    destroy_api = False
    destroy_dashboard = False

    match package:
        case InstallPackage.all:
            destroy_api = True
            destroy_dashboard = True
        case InstallPackage.api:
            destroy_api = True
        case InstallPackage.dashboard:
            destroy_dashboard = True

    hf_account = get_huggingface_account()

    if destroy_api:
        api_deploy_path = script_dir / "api/hf-deploy.yml"
        dep = load_huggingface_deployment(api_deploy_path)
        hf_account.destroy(dep)

    if destroy_dashboard:
        dashboard_deploy_path = script_dir / "dashboard/hf-deploy.yml"
        dep = load_huggingface_deployment(dashboard_deploy_path)
        hf_account.destroy(dep)

    print("Done")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    app()
