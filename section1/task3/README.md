# Task3 Get on-chain data from Ethercan & news from CryptoControl

In task2, you learned how to download data by REST API or simply using SDK. We've covered third-party data source like [CryptoCompare](https://www.cryptocompare.com/) and crypto-exchange like [Binance](https://www.binance.com/en). There're two other types of data could be used by investment research purposes: on-chain data and news.

This task will guide you to get on-chain data from [Etherscan](https://etherscan.io/) and news from [CryptoControl](https://cryptocontrol.io/en/)

## 1. Explore Etherscan data API

[Etherscan API Documentation](https://etherscan.io/apis#misc)

[Etherscan Python SDK Github Homepage](https://github.com/corpetty/py-etherscan-api)

Etherscan provides on-chain data in ethereum network, including block, account, transaction, erc20 contract and etc. On-chain data is regarded as "fundamental" in crypto world with compared to financial statement in stock market. Google and do some research if you're not familiar with on-chain analysis.

### Required

#### 1. **Use Etherscan Python SDK** to get on-chain data

Explore examples and tests in [Etherscan Python SDK Repo](https://github.com/corpetty/py-etherscan-api), play with those endpoints, print and take a look at the data you can get and figure out what it means, and do some basic formating.

**Write some scripts (.py file)**

- [x] play and combine scripts in examples/accounts
- [x] play and combine scripts in examples/blocks
- [x] play and combine scripts in examples/contracts
- [x] play and combine scripts in examples/proxies
- [x] play and combine scripts in examples/stats
- [x] play and combine scripts in examples/tokens
- [x] play and combine scripts in examples/transactions

Hint:

1. check its sdk repo: https://github.com/corpetty/py-etherscan-api, take a look at examples, tests and source codes. Find the specific endpoint you need.

### Optional

#### 1. learn Unittest in python

Unittest is normally used in software development regardless of programming language. Writing tests for your code not only makes it functionable and maintainable, but also clarifies its usage. Take a look at those tests in this repo: https://github.com/corpetty/py-etherscan-api/tree/master/tests.

Do some research on Google or maybe watch some videos in Youtube, learn:

1. Why write unittest code.
2. How to write unittests in python
3. How to setup unittest environment in your IDE (e.g. vscode)

Note:

1. There are 3 main unittest frameworks in python, unittest(built-in library), pytest and nose. Google them and compare, what are pros and cons?
2. Personally, I use pytest.

## 2. Explore CryptoControl data API

[CryptoControl API Documentation](https://cryptocontrol.io/en/developers/apis)

[CryptoControl Python SDK Github Homepage](https://github.com/cryptocontrol/python-api)

CryptoControl is one English free crypto-news provider. It covers
categoires like Analysis, Blockchain, Exchanges, General, Government, ICO and Mining news in crypto-world.

**Write a script (.py file)**

- [x] play and explore all endpoints provided
- [x] do some basic formating


### Work Log

#### 4/19

Reviewed code in task1 & task2. Finished some todos.

To update from a upstream, do `git fetch upstream` then `git merge upstream\master`

Use `solve conflict` to merge commits

#### 4/20

Forked repo [py-etherscan-api](https://github.com/corpetty/py-etherscan-api) to play with example files

As I was playing with Etherscan API, I was troubled by this response for a long time:
`etherscan.client.EmptyResponse: <Err: No transactions found>`.

After searching on google with no solution, I looked into the source code of `etherscan-api`. I found out that in module `etherscan.client` function `connect()`, when response status is not 1 the function will raise `EmptyResponse` without returning an empty json.

My solution is: I wrote a new class inherited `etherscan.client.Client` and override function `connect()`. Then I assigned `Client.connect` to this overridden function to keep etherscan-api functioning. This new class can be found in `EtherscanAPI.py` named `NewCient`

Also I encountered this response when I was playing with accounts APIs:
`etherscan.client.EmptyResponse: <Err: Result window is too large, PageNo x Offset size must be less than or equal to 10000>`.

I didn't fully understand the cause of this response. I tried to set offset lower and everything was fine. 

#### 4/21

As I was playing with Etherscan API, I found that I don't know the meaning of the most data. So I decided to stop coding and learn more about on-chain data on Google.

I found this article very helpful: [GUIDE TO CRYPTOCURRENCY VALUATION: A LOOK INTO ON-CHAIN DATA](https://masterthecrypto.com/guide-cryptocurrency-valuation-onchain-data/)



>Note taking:
>
>Typically, on chain data includes:
>
>* Details of every block (timestamp, gas price, miner, block size etc.)
>* Details of every transaction (The ‘from’ and ‘to’ addresses, the amount transferred in the transaction etc.)
>* Smart contract invocation and usage
>
> The on-chain transaction volume is being used to judge whether a given cryptoasset is actually being used.
>
> Use on-chain transaction data to figure out who are the entities that are actually using a given cryptoasset.
>
> Three clusterings:
>
>* Exchange-related addresses: Centralized cryptocurrency exchanges that generally have thousands of “hot wallets” that are used interchangeably to manage exchange operations and customer transactions. (See more: Crypto Guide 101: Choosing The Best Cryptocurrency Exchange)
>* “Bot” and “Burner” Addresses: Addresses that either display an “automated” transaction pattern — such as repetitive, similar transactions to and from the same recipient— or are clearly one-time-use “burner” addresses that only ever have one incoming and outgoing transaction.
>* Human-operated or “other” addresses: A catch-all bucket of addresses that generally display more irregular transaction patterns and show more variance in on-chain transactional relationships — hinting at an actual human being behind the address in question.
>
>When it comes to the world of crypto, aggregating addresses and classifying them into distinct entity types enables similarly nuanced analysis into the makeup of a given cryptoasset’s ecosystem.

Then I read about gas of ETH: [GUIDE TO ETHEREUM: WHAT IS GAS, GAS LIMIT AND GAS PRICE?](http://masterthecrypto.com/ethereum-what-is-gas-gas-limit-gas-price/)

>Note taking:
>
> Gas is used in ETH in order to measure the computational work of runnig transactions or smart contracts inthe Ethereum network.
> 
> Gas limit is the max amount of gas you are willing to spend on a particular transaction.
> 
> The more complex the commands you want to execute, the more gas you have to pay. 
>
> Gas limit acts as a safety mechanism to protect you from depleting your funds due to buggy codes or an error in the smart contract.
>
> If too little gas limit is set, miners will stop performing work on your transaction but keep the gas spent. Transaction 'Failed'
>
> Gas price: wei is smallest unit of Ether. Gwei is a billion wei
>
> * Std (Standard) Cost for Transfer: Average fees that users pay to transfer ETH – in USD value – for a standard priority transaction (usually a waiting time of fewer than 5 minutes)
> * Gas Price Std (Gwei): Average fees that users pay to transfer ETH – in Gwei value – for a standard priority transaction (usually a waiting time of fewer than 5 minutes)
> * SafeLow Cost for Transfer: Average fees that users pay to transfer ETH – in USD value – for a low priority transaction (usually a waiting time of fewer than 30 minutes)
> * Gas Price SafeLow (Gwei): Average fees that users pay to transfer ETH – in USD value – for a low priority transaction (usually a waiting time of fewer than 30 minutes)
> * Median Wait (s): Average waiting time for a single transaction in seconds
> * Median Wait (blocks): Average waiting time for a single transaction in blocks
> 
> If speed up transaction, user will pay higher gas price. 
>
> * Gas Limit: Maximum amount of gas that a user will pay for this transaction. The default amount for a standard ETH transfer is 21,000 gas
> * Gas Used by Txn: Actual amount of gas used to execute the transaction. Since this is a standard transfer, the gas used is also 21,000
> * Gas Price: Amount of ETH a user is prepared to pay for each unit of gas. The user chose to pay 8 Gwei for every gas unit, which is considered a “high priority” transaction and would be executed very fast
> * Actual Tx Cost Fee: This is the actual amount of fees that the user will pay for the transaction in Ether value (USD value is in brackets). Not bad; the user paid a total of 14 cents for his ETH to be transferred in less than 2 minutes!
> 
> Transaction (TX) fees: gas used by transaction * gas price
>
> one useful link: [ETH gas station](https://ethgasstation.info)

While I learn on google, I also found this website cool: [chainanalysis](https://www.chainalysis.com)


#### 4/22

Played with all apis of Etherscan SDK. I met some fatel errors that I can't fix.

`ModuleNotFoundError: No module named 'etherscan.blocks'`

`AttributeError: 'Proxies' object has no attribute 'gas_price'`

`AttributeError: 'Proxies' object has no attribute 'get_code'`

`AttributeError: 'Proxies' object has no attribute 'gas_storage_at'`

`ModuleNotFoundError: No module named 'etherscan.transactions'`

I saved account data in csv format in AccountData folder.

I saved other data I retrived in json format. I think json is enough for now and I need some guidence on what data should I be looking for. 

Played with Crypto Control API. Saved all data in json format.

Finished Task 3 without optional task -- unittesting

I will learn unit testing on 4/23

#### 4/23

Learned unit testing

Read this page: [Blockchain Super FAQ](https://consensys.net/knowledge-base/blockchain-super-faq/)