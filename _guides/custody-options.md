---
title: "Custody options: multisig vs custodian"
layout: guide
weight: 5
description: "How your company holds Bitcoin matters more than what it holds. This guide compares self-custody with shared approvals and regulated custodians, and helps you choose for your risk level."
author: banitama
reviewer: faizal

reading_time: 8
last_modified_at: 2026-10-29
thumbnail: "images/thumbs/custody-options.png"
thumbnail_alt: "A vault door with a gold dial"
---

Most losses in Bitcoin trace back to custody, not to the network. Who holds the keys, and under what rules, is the central operational decision of a Bitcoin treasury.

This guide compares the options. Custody is not a product you buy. It is a set of decisions you make and then prove.

## Who this is for

CFOs, IT and security leads and anyone who will be responsible for how the company's Bitcoin is held.

## The core idea

Bitcoin is controlled by private keys. Whoever can use the keys controls the funds. Custody design is therefore about answering three questions: who holds the keys, how many must agree before funds move, and what happens when something goes wrong.

## The three main models

| Model | How it works | Strengths | Weaknesses |
| --- | --- | --- | --- |
| Single key, self-held | One person or device holds the key | Simple | One loss or theft ends the treasury. Not suitable for a company |
| Multi-signature self-custody | Several keys held by different people and places, with a threshold such as 3 of 5 needed to move funds | No single point of failure, no third-party dependency | Needs procedures, training and regular drills |
| Regulated custodian | A licensed provider holds the assets on your behalf | Professional security, insurance options, audit reports | You depend on the provider, and their failure or legal problems become yours |

<figure><img src="{{ 'images/figures/custody-options-1.svg' | relative_url }}" alt="Single key, multisig self-custody and regulated custodian, arranged from more control and more work for you to less work and more reliance on others." loading="lazy"><figcaption>The trade-off is control against operational burden. Neither end is free.</figcaption></figure>

Many companies use a hybrid, for example a custodian that holds some of the keys in a shared-approval arrangement, so that neither the company nor the provider can act alone.

## How to choose

Ask these questions in order:

1. **How much are we holding relative to our reserves?** Larger amounts justify more professional arrangements.
2. **Do we have people who can run key procedures reliably?** If not, a custodian reduces operational risk.
3. **What do our auditors, insurers and regulators expect?** Some require a regulated custodian.
4. **How will we recover if people leave or devices fail?** The answer must be written and tested.
5. **What would a custodian failure cost us?** Check their licensing, reserves, insurance and legal structure, and what happens to your assets in insolvency.

## Setting up multi-signature custody

1. Decide the threshold and the number of keys, for example three of five.
2. Assign keys to different people in different locations, ideally on different types of hardware.
3. Write the approval procedure, including who proposes, who approves and what is verified before signing.
4. Make backups of each key, store them offline in separate places and record where they are.
5. Run a recovery drill: move a small amount, restore from backups and confirm it works.
6. Plan for succession: who takes over each role, and how keys are rotated when someone leaves.

<figure><img src="{{ 'images/figures/custody-options-2.svg' | relative_url }}" alt="Five recovery drill steps: move a small amount, wipe a signer, restore from backup, sign again and record the result." loading="lazy"><figcaption>The recovery drill. A backup you have not restored is a belief, not a backup.</figcaption></figure>

## Buying the devices

Self-custody starts before the first transaction. The attack often happens before the box reaches you.

- **Buy from the manufacturer** or a reseller the manufacturer lists. Every extra hop is a stranger.
- **Treat packaging as a filter, not proof.** Seals can be restored.
- **Never accept a device that arrives with a seed phrase,** or asks you to import one.
- **Generate the seed yourself,** on the device, in private.
- **Spread vendors.** Keys on devices from different makers mean no single supply chain decides the outcome.

The full list is in [Hardware wallet supply-chain safety](https://banitama.my.id/insights/hardware-wallet-supply-chain-safety). A recent tampering case is covered in [The Ledger reseller attack](https://banitama.my.id/insights/ledger-reseller-attack).

## Choosing a custodian

If you use a regulated custodian, ask in writing:

1. Which licence do they hold, and from which regulator?
2. How are client assets held and separated from the firm's?
3. What happens to your assets if the firm fails?
4. What insurance exists, and what does it actually cover?
5. Which independent reports can you read?

## Common mistakes

- Leaving funds on a trading platform.
- Keeping all backups in one location.
- Never testing recovery.
- No plan for when a key-holder resigns.
- Choosing a custodian without checking licensing, insurance and insolvency treatment.
- Buying a device from a marketplace seller of unknown origin.

## Checklist

- Custody model chosen and documented
- Keys held by different people in different places
- Approval procedure written
- Backups made and verified
- Recovery drill completed
- Succession plan for each key-holder

## The bottom line

Custody is not a product you buy so much as a chain you accept. Every link you remove, verify or test is one an attacker cannot use.

Pick the model that fits your people and your size. Then write it down and run the drill.

Legal and tax questions about custody, such as who legally holds the asset, stay with your own qualified advisers.

## Sources

- [Multisignature, Bitcoin Wiki](https://en.bitcoin.it/wiki/Multisignature)
- [Hardware wallet supply-chain safety, Banitama](https://banitama.my.id/insights/hardware-wallet-supply-chain-safety)
- [The Ledger reseller attack, Banitama](https://banitama.my.id/insights/ledger-reseller-attack)
