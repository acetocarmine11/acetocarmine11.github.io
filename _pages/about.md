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

I am a junior student at School of Electronics Engineering and Computer Science, Peking University. My research interests lie in the development of human-like intelligent agents, with a particular focus on understanding and interpreting their behavior to enhance model control and optimize performance. While my prior work has predominantly been rooted in theoretical research, I am equally passionate about exploring the engineering aspects, aiming to bridge the gap between theoretical advancements and practical implementations to drive more robust, efficient, and human-aligned AI systems.

<!-- You can find my publications on <a href='https://scholar.google.com/citations?hl=en&user=f7KQvukAAAAJ'>Google Scholar <img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>. -->

<span style="color: #f4b400">I am currently looking for 2026 fall PhD opportunities!!!</span>

<span style="color: #4285f4">I will attend ICLR 2025, feel free to reach out!</span>

# 🔥 News
- *2025.04*: &nbsp;🎤 Our recent work "When More is Less: Understanding Chain-of-Thought Length in LLMs" has been selected as an <span style="color: red">Oral presentation</span> at ICLR 2025 Workshop on Reasoning and Planning for LLMs!
- *2025.03*: &nbsp;🎉 Our paper "When More is Less: Understanding Chain-of-Thought Length in LLMs" is accepted to ICLR 2025 Workshop on Reasoning and Planning for Large Language Models!
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

[When More is Less: Understanding Chain-of-Thought Length in LLMs](https://arxiv.org/abs/2502.07266v1)

**Yuyang Wu\***, Yifei Wang\*, Tianqi Du, Stefanie Jegelka, Yisen Wang

<!-- [**Paper**](https://arxiv.org/abs/2502.07266v1) -->
- <span style="color: red">Oral presentation at ICLR 2025 Workshop on Reasoning and Planning for LLMs</span>
- I mathematically model the CoT process as a task decomposition and subtask-solving procedure and demonstrate that a longer CoT is not necessarily better.
- Additionally, I conduct both synthetic and real-world experiments, revealing a U-shaped curve and the scaling behavior of the optimal CoT length.
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
- *2024.06* <span style="color: red">Best Paper Award at ICML 2024 Workshop on In-context Learning</span>
- *2021.12* Silver Medal, Chinese Mathematical Olympiad

# 📖 Education
- *2022.09 - Present*, **Peking University**, BS in Computer Science

# 💻 Research Experience
- *2023.10 - Present*, Research Intern at ZERO Lab, Peking University
  - Researching the in-context abilities in LLMs, including self-correction and chain-of-thought.
  - Collaborating with Postdoc [Yifei Wang (MIT)](https://yifeiwang77.com) and advised by Prof. [Yisen Wang (PKU)](https://yisenwang.github.io)

- *2025.3 - Present*, Research Intern at Sky Computing Lab, UC Berkeley
  - Researching on meta-reasoning ability in LLMs.
  - Collaborating with [Dacheng Li](https://dachengli1.github.io) and advised by Prof. [Ion Stoica](https://people.eecs.berkeley.edu/~istoica/)

# 💪 Skills
- **Programming Languages**: Python(proficient), C++(proficient), C#, Core Skills (Git/Linux/TeX/etc.)
- **Deep Learning Technologies**: Pytorch(proficient), CUDA parallel programming