from diagrams import Diagram, Cluster
from diagrams.aws.compute import ECS
from diagrams.aws.database import Dynamodb
from diagrams.aws.network import APIGateway, ELB
from diagrams.aws.storage import S3
from diagrams.onprem.client import User
from diagrams.generic.device import Mobile
from diagrams.onprem.network import Internet
from diagrams.custom import Custom

with Diagram("Extended Mini Switch System Architecture with Prefunded Wallet", show=False, direction="LR", graph_attr={"size": "10,10"}):
    user = User("End User")
    mobile = [Mobile("Android App"), Mobile("iOS App")]

    with Cluster("AWS Cloud Infrastructure"):
        with Cluster("API Services"):
            api_gateway = APIGateway("API Gateway")
            load_balancer = ELB("Load Balancer")

        with Cluster("Data Storage"):
            ledger_db = Dynamodb("Transaction Ledger")
            file_storage = S3("File Storage")

        with Cluster("Application Services"):
            app_service = ECS("Application Service")

    with Cluster("Blockchain Integration"):
        sui = Custom("SUI Blockchain", "./path-to-sui-icon.png")
        stablecoin_provider = Custom("Stablecoin Provider", "./path-to-stablecoin-icon.png")
        prefunded_wallet = Custom("Prefunded Wallet", "./path-to-wallet-icon.png")

    with Cluster("Local Cash-out Agents"):
        bank_of_khartoum = Custom("Bank of Khartoum", "./path-to-bank-icon.png")
        mtn = Custom("MTN Agent", "./path-to-mtn-icon.png")

    internet = Internet("Internet")

    user >> mobile >> api_gateway >> load_balancer >> app_service
    app_service >> ledger_db
    app_service >> file_storage
    app_service >> sui >> stablecoin_provider >> prefunded_wallet
    mobile >> internet >> [bank_of_khartoum, mtn]
