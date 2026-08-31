---
title: "Stealth design notes"
parent: "ghilliesuit"
---

These notes cover the stealth system in code, building on the overview on the main page.

## The stealth math

The per-piece reduction is a multiplier of one eighth, applied to the visibility value the targeting system uses, so a full suit multiplies by one half. That is why the reduction is proportional across mobs. A standard hostile mob with a **16**-block follow range is cut to **8** blocks, a zombie family mob at **35** to **17.5**, a Blaze at **48** to **24**, an Enderman at **64** to **32**, and a Ghast at **100** to **50**. The percentage is the constant, and the starting range only changes the numbers.

## How the crouch works

Two mixins make the crouch. The first hooks `TargetingConditions`, the object mobs use to pick targets, and makes its `test` method return false when the wearer has the full suit and is crouching, so mobs never acquire you in the first place. The second hooks `Mob.asValidTarget`, the shared path for both `getTarget` and `setTarget`, and rejects the stealthed wearer there, which clears an existing chase the moment you crouch and stops it being re-acquired. That is why a mob mid-chase drops you instantly instead of resuming.

## Why other players still see you

The crouch applies the game's Invisibility effect, in code `MobEffects.INVISIBILITY`, but the rendering is changed so the wearer shows as a translucent ghost rather than vanishing, the way spectators appear. The effect is granted for **200** ticks, which is ten seconds, and it is refreshed while you stay crouched, so it never lapses mid-hide. It is removed the moment you stop.

## A singleplayer quirk

Removing the effect needs a per-instance flag because of how singleplayer runs. The client and the integrated server tick separate instances of the same player in one JVM, so a shared set of players to clean up after would break, since whichever side ticks first would consume the entry and leave the other side's local effect stuck. The per-instance flag also means the mod only ever removes the invisibility it applied, never one from a potion.

## What it taught me

Making the mod taught me how to make a mod in Fabric. It was also the first project where I used proper version tags in the CI pipeline, with the release workflow bumping the patch version and cutting a tagged release on every push to main. I plan to carry that habit into future projects, and it started me thinking more about Git commit etiquette.
