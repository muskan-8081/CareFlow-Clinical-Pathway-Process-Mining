# CareFlow Project - Transition Analysis Report

## Overview
This report documents the transition analysis performed on the CareFlow clinical pathway dataset. By mapping consecutive activity pairs across patient cases (`A`, `AA`, `AAA`, `AB`, `ABA`), we identify standard care trajectories and frequent diagnostic routing sequences.

## Transition Frequency Summary

| Transition Pair | Total Count | Observation |
| :--- | :---: | :--- |
| ER Registration → ER Triage | 5 | Standard admission sequence for all evaluated cases |
| ER Triage → ER Sepsis Triage | 5 | Universal escalation pathway for emergency assessment |
| ER Sepsis Triage → CRP | 4 | Primary diagnostic lab order following triage |
| CRP → Leucocytes | 2 | Standard secondary lab panel progression |
| Leucocytes → CRP | 1 | Repeated diagnostic tracking sequence |
| ER Sepsis Triage → Leucocytes | 1 | Direct jump to leucocyte evaluation |

## Key Findings & Next Steps
- **Primary Bottleneck / Main Path**: The most frequent deterministic path is `ER Registration` → `ER Triage` → `ER Sepsis Triage` → `CRP`, occurring consistently across the initial evaluation stages.
- **Variability**: Cases such as `AA` and `AAA` exhibit iterative lab sequences (`Leucocytes ⇄ CRP`), indicating tailored diagnostic monitoring for complex presentations.
- **Next Actions**: Integrate these transition counts into the broader process mining model to evaluate temporal durations between states.