---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

My long-term goal is to contribute to progress toward artificial superintelligence. I study how large language models reason and use context. My approach is to use theory to formalize intuitions and explain empirical behavior, then translate these insights into better methods and practical guidance. My work examines when and how LLMs can self-correct, what determines optimal reasoning length, and how rotary position embeddings (RoPE) shape long-context behavior.

Drawing on machine learning fundamentals, I am also interested in principled data selection and adaptive compute allocation: which data a model can learn from most effectively, and where additional computation is most useful.

You can find my publications on <a href='https://scholar.google.com/citations?hl=en&user=f7KQvukAAAAJ'>Google Scholar <img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.

<span style="color: #f4b400">I am actively seeking PhD opportunities for Fall 2027.</span>


# 🔥 News
- *2026.01*: &nbsp;🎉 Our paper "When More is Less: Understanding Chain-of-Thought Length in LLMs" has been accepted at **ICLR 2026**!
- *2025.04*: &nbsp;🏆 Our work "When More is Less: Understanding Chain-of-Thought Length in LLMs" received the <span style="color: red">Best Paper Runner-Up Award</span> at the ICLR 2025 Workshop on Reasoning and Planning for Large Language Models!
- *2025.04*: &nbsp;🎤 I will give an oral presentation on our work "When More is Less: Understanding Chain-of-Thought Length in LLMs" at the ICLR 2025 Workshop on Reasoning and Planning for Large Language Models!
- *2024.12*: &nbsp;🍁 I attended NeurIPS 2024 in Vancouver and presented our poster.
- *2024.10*: &nbsp;🎉 Our paper "A Theoretical Understanding of Self-Correction through In-context Alignment" has been accepted at **NeurIPS 2024**!
- *2024.06*: &nbsp;🏆 "A Theoretical Understanding of Self-Correction through In-context Alignment" received the <span style="color: red">Best Paper Award</span> at the ICML 2024 Workshop on In-Context Learning!

# 📝 Publications 

(* denotes equal contribution.)

<div class='paper-box'><div class='paper-box-image'><div class="paper-visual">
<div class="venue-badge venue-badge--iclr" aria-label="ICLR 2026">
    <span class="venue-badge__mark" aria-hidden="true"></span>
    <span class="venue-badge__name">ICLR</span>
    <span class="venue-badge__year">2026</span>
</div>
<img src='images/cot_poster.png' alt="Poster for When More is Less" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[When More is Less: Understanding Chain-of-Thought Length in LLMs](https://openreview.net/forum?id=6QDFsYxtI1)

**Yuyang Wu\***, Yifei Wang\*, Ziyu Ye, Tianqi Du, Stefanie Jegelka, Yisen Wang

<!-- [**Paper**](https://openreview.net/forum?id=6QDFsYxtI1) -->
- <span style="color: red">Best Paper Runner-Up Award at the ICLR 2025 Workshop on Reasoning and Planning for Large Language Models (200+ citations)</span>
- We revealed two counterintuitive findings: longer CoTs are not always better, and during reinforcement learning, models exhibit a **simplicity bias**, converging to the shortest effective CoT.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div class="paper-visual">
<div class="venue-badge venue-badge--neurips" aria-label="NeurIPS 2024">
    <span class="venue-badge__mark" aria-hidden="true"></span>
    <span class="venue-badge__name">NeurIPS</span>
    <span class="venue-badge__year">2024</span>
</div>
<img src='images/self_correction.png' alt="Overview of in-context self-correction" width="100%">
</div></div>
<div class='paper-box-text' markdown="1">

[A Theoretical Understanding of Self-Correction through In-context Alignment](https://openreview.net/pdf?id=OtvNLTWYww)

Yifei Wang\*, **Yuyang Wu\***, Zeming Wei, Stefanie Jegelka, Yisen Wang

<!-- [**Paper**](https://openreview.net/pdf?id=OtvNLTWYww) -->
- <span style="color: red">Best Paper Award at the ICML 2024 Workshop on In-Context Learning</span>
- We provided the first rigorous theoretical account of LLM self-correction and developed CaC, a simple and efficient self-correction algorithm that achieves significant improvements across multiple tasks.
</div>
</div>

# 🎖 Honors and Awards
- *2026.06* Peking University Outstanding Undergraduate Thesis Award (Top 10 in the School of Electronics Engineering and Computer Science)
- *2025.04* Best Paper Runner-Up Award at the ICLR 2025 Workshop on Reasoning and Planning for Large Language Models
- *2024.06* Best Paper Award at the ICML 2024 Workshop on In-Context Learning
- *2021.12* Silver Medal, Chinese Mathematical Olympiad

# 🎤 Talks
- *2025.04* "When More is Less: Understanding Chain-of-Thought Length in LLMs" - Oral presentation at the ICLR 2025 Workshop on Reasoning and Planning for Large Language Models in Singapore

# 📖 Education
- *2022.09 - 2026.07*, **Peking University**, B.S. in Computer Science

# 💻 Research Experience
- *2026.05 - Present*, Research Intern in Prof. Hao Peng's Group, **UIUC**
  - Studying long-context capabilities through RoPE.
  - Collaborating with [Yufeng Du](https://openreview.net/profile?id=~Yufeng_Du2) under the supervision of Prof. [Hao Peng](https://haopeng-nlp.github.io).

- *2025.03 - 2025.06 (ended due to nonacademic circumstances)*, Research Intern at Sky Computing Lab, **UC Berkeley**
  - Studied meta-reasoning capabilities in LLMs.
  - Collaborated with [Dacheng Li](https://dachengli1.github.io) under the supervision of Prof. [Ion Stoica](https://people.eecs.berkeley.edu/~istoica/).

- *2023.10 - 2026.06*, Research Intern at ZERO Lab, **Peking University**
  - Studied the in-context learning capabilities of LLMs, including self-correction and chain-of-thought reasoning.
  - Collaborated with [Yifei Wang (MIT)](https://yifeiwang77.com) under the supervision of Prof. [Yisen Wang (PKU)](https://yisenwang.github.io).
