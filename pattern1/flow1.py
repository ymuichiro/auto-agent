from autogen import ConversableAgent
from pattern1.libs.config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT_NAME,
    AZURE_OPENAI_ENDPOINT,
)

llm_config = {
    "api_type": "azure",
    "api_version": "2024-02-15-preview",
    "api_key": AZURE_OPENAI_API_KEY,
    "base_url": AZURE_OPENAI_ENDPOINT,
    "model": AZURE_OPENAI_DEPLOYMENT_NAME,
}

agent1 = ConversableAgent(
    "金融系Web3評論家",
    system_message="\n".join(
        [
            "あなたは金融機関に務めるWeb3の評論家です。",
            "Web3についてあなたの意見を述べて下さい。",
            "相手のコメントは出来るだけそのまま使わないで返信します。",
            "相手からの返信に対しては出来るだけ自身の見解と相違があれば反論を行い、出来るだけ会話を続けてください。",
        ]
    ),
    llm_config=llm_config,
    code_execution_config=False,
    function_map=None,
    # is_termination_msg=lambda msg: "終了" in msg["content"],
    human_input_mode="ALWAYS",
)

agent2 = ConversableAgent(
    "ビジネス系Web3評論家",
    system_message="\n".join(
        [
            "あなたは多くの企業を経営する起業家です。起業家目線でWeb3についての意見を述べてください。",
            "Web3についてあなたの意見を述べて下さい。",
            "相手からの返信に対しては出来るだけ自身の見解と相違があれば反論を行い、出来るだけ会話を続けてください。",
            "相手のコメントは出来るだけそのまま使わないで返信します。",
        ]
    ),
    llm_config=llm_config,
    code_execution_config=False,
    function_map=None,
    human_input_mode="NEVER",
    # is_termination_msg=lambda msg: "終了" in msg["content"],
)

result = agent1.initiate_chat(
    agent2,
    message="Web3は人類の役に立ちましたか？また、人類の生活をどのように変革しますか？",
    max_turns=10,
)
