---
title: "\"If we lose the keys, it's gone.\""
layout: myth
weight: 9
description: "True when one person holds one key. A signing quorum, tested backups and written roles make a single loss survivable. The process matters more than the tool."
author: banitama
reviewer: ricky
related_guide: custody-options
reading_time: 4
last_modified_at: 2026-10-29
thumbnail: "images/thumbs/lose-the-keys-gone.png"
thumbnail_alt: "Three keys pointing at one padlock"
---

## Losing a key is not the failure. Having only one is.

Yes, if the only key is lost, the Bitcoin is gone. There is no support desk that can reset it. That is the trade for not depending on anyone.

But a company that stores its Bitcoin behind one device, held by one person, has built a single point of failure. It did not need Bitcoin to do that.

## What is true in the myth

Bitcoin is controlled by whoever can produce the right signatures. There is no "forgot password." A lost key, a destroyed backup or a person who leaves with the only copy are all real ways to lose funds.

Nothing below changes that. It changes how many things must go wrong at once.

## Where the myth breaks down

The fix is not a better device. It is a **signing quorum**: several keys, held by different people in different places, with a threshold needed to move funds.

<figure><img src="{{ 'images/figures/lose-the-keys-gone-1.svg' | relative_url }}" alt="Three keys held by the finance director, the chief executive and an independent holder in different places. Any two can approve a move from the company wallet." loading="lazy"><figcaption>A 2-of-3 setup. Lose one key and the treasury still moves. An example layout, decided in your policy.</figcaption></figure>

In a 2-of-3 setup, any two keys can approve a transaction. Lose one and you still move funds. A thief who steals one key still cannot. This is called [multisignature](https://en.bitcoin.it/wiki/Multisignature), and it is how many organisations remove the single point of failure.

## What makes it work

A quorum on its own is not enough. It needs four things around it.

1. **Roles.** Who holds each key, and who is the successor if they leave.
2. **Backups.** Each key backed up offline, in separate places, with the locations recorded.
3. **A written approval process.** Who proposes, who approves, and what they check before signing.
4. **A recovery drill.** Move a small amount, restore from backup alone, and sign again.

Skip the drill and you only believe your backup works. Run it and you know.

<figure><img src="{{ 'images/figures/custody-options-2.svg' | relative_url }}" alt="Five recovery drill steps: move a small amount, wipe a signer, restore from backup, sign again and record the result." loading="lazy"><figcaption>The recovery drill. If any step fails, fix the procedure and repeat.</figcaption></figure>

## The part that surprises people

The weakest link is usually a person, not a device. One person who knows everything. One backup in one drawer. One process that lives in someone's head.

A tool cannot fix that. A written process can.

## A better question

> If any one of our key-holders disappeared tomorrow, could we still move the funds on Monday?

If the answer is "I think so," you have not tested it yet.

## What we do with your team

We design the quorum with you, write the roles and procedures, and run the first recovery drill together. [The custody guide]({{ '/guides/custody-options/' | relative_url }}) lays out the choices. We never hold your keys, seed phrases or coins.

## Sources

- [Multisignature, Bitcoin Wiki](https://en.bitcoin.it/wiki/Multisignature)
