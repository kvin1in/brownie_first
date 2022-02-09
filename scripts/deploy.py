import os

from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    account = accounts.add(config["wallets"]["from_key"])
    simple_storage = SimpleStorage.deploy({"from": account})
    transaction = simple_storage.store(33, {"from": account})
    transaction.wait(1)
    updated_store_value = simple_storage.retrieve()
    print(updated_store_value)

def main():
    deploy_simple_storage()