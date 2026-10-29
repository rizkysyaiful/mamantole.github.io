---
title: "\"Bitcoin gets hacked.\""
layout: myth
weight: 8
description: "The network and the places people keep Bitcoin are different risks. Most headline losses come from exchanges, devices and bad process, not from the protocol. Custody design is the answer."
author: banitama
reviewer: ricky
related_guide: custody-options
reading_time: 4
thumbnail: "images/thumbs/bitcoin-gets-hacked.png"
thumbnail_alt: "A shield with a gold checkmark"
---

## The headline is true. The sentence is wrong.

Money has been stolen. That is true. "Bitcoin gets hacked" is still the wrong sentence, because it hides where the theft happened.

Ask the useful question instead: what exactly was attacked?

## What is true in the myth

People have lost large amounts of Bitcoin. Exchanges have failed or been breached. Hardware has been tampered with. Employees have been tricked. Keys have been lost.

None of that is imaginary, and a company should assume it can happen to them if they are careless.

## Where the myth breaks down

Bitcoin is not one system. It is three layers, and each layer fails in a different way.

<figure><img src="{{ 'images/figures/bitcoin-gets-hacked-1.svg' | relative_url }}" alt="Three layers: the network, exchanges and wallet software, and people and process, with the type of risk at each layer." loading="lazy"><figcaption>The network, the platforms and devices, and the people. Most losses sit in the second and third layers.</figcaption></figure>

**The network.** Consensus rules and the ledger. This layer has run since 2009. The design is public, in the [original paper](https://bitcoin.org/bitcoin.pdf), and has been attacked and reviewed for years.

**Exchanges and wallet software.** Platforms, apps and devices. This is where most of the well-known losses sit. [Mt. Gox](https://en.wikipedia.org/wiki/Mt._Gox) lost customers' coins in 2014. That was one company's failure, not the protocol's.

**People and process.** Who holds the keys, who approves a transfer, who checks. Phishing, a single person with too much power, and no recovery plan live here.

Hardware is a good example. We covered a recent case: genuine devices were tampered with on their way to buyers. It was [a distribution failure, not a cryptography failure](https://banitama.my.id/insights/ledger-reseller-attack). The fix was to change how people buy and verify devices.

## What custody design does

It answers each layer on purpose.

1. **Do not leave funds on a platform you cannot audit.** Know whose promise you are relying on.
2. **Buy devices from the maker.** Verify them before use. [A practical buying guide](https://banitama.my.id/insights/hardware-wallet-supply-chain-safety) lists six rules.
3. **Remove single points of failure.** Several keys, held by different people, in different places.
4. **Write the process down.** Who proposes, who approves, who checks.

None of that makes the risk zero. It makes the risk **known and owned**.

## A better question

> If something goes wrong, which layer failed, and what did we put in place to catch it?

If your team can answer that for each layer, the headline is no longer about you.

## What we do with your team

We map your setup against the three layers, find the single points of failure, and design a custody arrangement that fits your people and your size. [The custody guide]({{ '/guides/custody-options/' | relative_url }}) shows the options. We never hold your keys, seed phrases or coins. That is a rule.

## Sources

- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf)
- [Mt. Gox, overview](https://en.wikipedia.org/wiki/Mt._Gox)
- [The Ledger reseller attack, Banitama](https://banitama.my.id/insights/ledger-reseller-attack)
- [Hardware wallet supply-chain safety, Banitama](https://banitama.my.id/insights/hardware-wallet-supply-chain-safety)
