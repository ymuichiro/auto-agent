from semantic_kernel.kernel import Kernel
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (
    AzureChatPromptExecutionSettings,
)

from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import (
    AzureChatCompletion,
)

from pattern1.libs.config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT_NAME,
    AZURE_OPENAI_ENDPOINT,
)

service_id = "default"

kernel = Kernel()
kernel.add_service(
    service=AzureChatCompletion(
        service_id=service_id,
        deployment_name=AZURE_OPENAI_DEPLOYMENT_NAME,
        endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
    )
)


def get_default_config():
    config = kernel.get_prompt_execution_settings_from_service_id(service_id)

    if isinstance(config, AzureChatPromptExecutionSettings):
        config.max_tokens = 1000
        return config

    raise ValueError("Invalid configuration")


def get_default_service():
    service = kernel.get_service(service_id)

    if isinstance(service, AzureChatCompletion):
        return service

    raise ValueError("Invalid service")
