from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor
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

# work_dir = ""

executor = LocalCommandLineCodeExecutor(
    timeout=10,
    work_dir=work_dir,
)


# コードの作成者と実行者は分離する。以下はコード推論 Agent。LLM を持つ。
code_writer_agent = ConversableAgent(
    "code-writer",
    system_message="\n".join(
        [
            "あなたはPython開発者です。",
            "あなたがコードを書くと自動的に外部のアプリケーション上で実行されます。",
            "ユーザーの指示に従ってあなたはコードを書きます。",
            "コードの実行結果は、あなたがコードを投稿した後に自動的に表示されます。",
            "ただし、次の条件を厳密に遵守する必要があります。",
            "ルール:",
            "1. コードブロック内でのみコードを提案します。",
            "2. あなたが作成するスクリプトは、'./' に保存されます。",
            "3. あなたが作成したスクリプトが操作する対象のアプリケーションは、 '../target_dir' にインストールされています。",
            "4. スクリプトの実行結果がエラーである場合、エラー文を元に対策を考え、修正したコードを再度作成します。"
            "5. スクリプトを実行した結果、情報を十分に得られなかった場合、現状得られた情報から修正したコードを再度作成します。",
            "6. あなたはユーザーの指示を最終目標とし、これを満たす迄何度もコードを作成・修正します。",
            "7. 目的を達成した場合、終了、とユーザーに伝えます。",
        ]
    ),
    llm_config=llm_config,
    code_execution_config=False,
    function_map=None,
    is_termination_msg=lambda msg: "終了" in msg,
    human_input_mode="ALWAYS",
)

# コードの作成者と実行者は分離する。以下はコード実行者 Agent。LLM は持たない。
code_execution_agent = ConversableAgent(
    "code-execution",
    llm_config=False,
    code_execution_config={"executor": executor},
    human_input_mode="ALWAYS",
)

user_message = "\n".join(
    [
        "'../target_dir' にはとあるアプリケーションのソースコードがあります。",
        "そのソースコードのファイルを確認して、何のアプリケーションかを推測してください。",
    ]
)

code_execution_agent.initiate_chat(code_writer_agent, message=user_message)

# work_dir をクリアする
import os
import shutil

shutil.rmtree(work_dir)
os.mkdir(work_dir)
