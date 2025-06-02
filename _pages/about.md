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

My research interest lies in developing a mathematical understanding of LLMs, interpreting their diverse behaviors, and providing principled theoretical guidance for the design and optimization of system-2 reasoning agents. Specifically, my approach involves expanding reasoning boundaries, e.g. enabling effective long-context reasoning and precise multi-round backtracking, and calibrating reasoning skills into practical experience via reinforcement learning in the post-training stage.
You can find my publications on <a href='https://scholar.google.com/citations?hl=en&user=f7KQvukAAAAJ'>Google Scholar <img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.

<span style="color: #f4b400">I am currently looking for 2025 summer intern opportunities!!!</span>


# 🔥 News
- *2025.04*: &nbsp;🏆 Our recent work "When More is Less: Understanding Chain-of-Thought Length in LLMs" has been awarded the <span style="color: red">Best Paper Runner-up Award</span> at ICLR 2025 Workshop on Reasoning and Planning for LLMs!
- *2025.04*: &nbsp;🎤 I will present an oral talk on our recent work "When More is Less: Understanding Chain-of-Thought Length in LLMs" at ICLR 2025 Workshop on Reasoning and Planning for LLMs!
- *2024.12*: &nbsp;🍁 I attended NuerIPS 2024 at Vancouver and illustrated our poster.
- *2024.10*: &nbsp;🎉 Our paper "A Theoretical Understanding of Self-Correction through In-context Alignment" has been accepted to **NeurIPS 2024**!
- *2024.06*: &nbsp;🏆 "A Theoretical Understanding of Self-Correction through In-context Alignment" received the <span style="color: red">Best Paper Award</span> at ICML Workshop on In-context Learning!

# 📝 Publications 

(*: Equal Contribution)

<style>
.badge-container {
    display: flex;
    flex-direction: column;
    gap: 5px;
    margin-bottom: 10px;
}
.badge {
    display: inline-block;
    padding: 0.25em 0.4em;
    font-size: 75%;
    font-weight: 700;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: 0.25rem;
}
.badge.neurips {
    background-color: #4285f4;
    color: white;
}
.badge.icml {
    background-color: #f4b400;
    color: black;
}
</style>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR-W'25</div><img src='images/cot_poster.png' alt="cot_poster" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[When More is Less: Understanding Chain-of-Thought Length in LLMs](https://arxiv.org/abs/2502.07266)

**Yuyang Wu\***, Yifei Wang\*, Ziyu Ye, Tianqi Du, Stefanie Jegelka, Yisen Wang

<!-- [**Paper**](https://arxiv.org/abs/2502.07266) -->
- <span style="color: red">Best Paper Runner-Up Award at ICLR 2025 Workshop on Reasoning and Planning for Large Language Models.</span>
- We revealed two counterintuitive findings: longer CoTs are not always better, and during reinforcement learning, models exhibit a **simplicity bias**, converging to the shortest CoT they can effectively manage.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div>
<div class="badge-container">
    <div class="badge neurips">NeurIPS 2024</div>
    <!-- <div class="badge icml">Best Paper Award at ICML-W'24</div> -->
</div>
<img src='images/self_correction.png' alt="self_correction" width="100%">
</div></div>
<div class='paper-box-text' markdown="1">

[A Theoretical Understanding of Self-Correction through In-context Alignment](https://openreview.net/pdf?id=OtvNLTWYww)

Yifei Wang\*, **Yuyang Wu\***, Zeming Wei, Stefanie Jegelka, Yisen Wang

<!-- [**Paper**](https://openreview.net/pdf?id=OtvNLTWYww) -->
- <span style="color: red">Best Paper Award at ICML 2024 Workshop on In-context Learning</span>
- I established the first rigorous understanding of LLMs' self-correction ability and developed a simple and efficient self-correction algorithm (CaC) that shows significant improvements across different tasks.
</div>
</div>

# 🎖 Honors and Awards
- *2025.04* Best Paper Runner-up Award at ICLR 2025 Workshop on Reasoning and Planning for LLMs
- *2024.06* Best Paper Award at ICML 2024 Workshop on In-context Learning
- *2021.12* Silver Medal, Chinese Mathematical Olympiad

# 🎤 Talks
- *2025.04* "When More is Less: Understanding Chain-of-Thought Length in LLMs", Oral presentation at ICLR 2025 Workshop on Reasoning and Planning for Large Language Models, Singapore

# 📖 Education
- *2022.09 - Present*, **Peking University**, BS in Computer Science

# 💻 Research Experience
- *2023.10 - Present*, Research Intern at ZERO Lab, Peking University
  - Researching the in-context abilities in LLMs, including self-correction and chain-of-thought.
  - Collaborating with Postdoc [Yifei Wang (MIT)](https://yifeiwang77.com) and advised by Prof. [Yisen Wang (PKU)](https://yisenwang.github.io)

- *2025.3 - 2025.6 (terminated due to non-academic political reasons)*, Research Intern at Sky Computing Lab, UC Berkeley 
  - Researching on meta-reasoning ability in LLMs.
  - Collaborating with [Dacheng Li](https://dachengli1.github.io) and advised by Prof. [Ion Stoica](https://people.eecs.berkeley.edu/~istoica/)

# 💪 Skills
- **Programming Languages**: Python(proficient), C++(proficient), C#, Core Skills (Git/Linux/TeX/etc.)
- **Deep Learning Technologies**: Pytorch(proficient), CUDA parallel programming