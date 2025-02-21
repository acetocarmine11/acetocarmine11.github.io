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

I am deeply fascinated by the development of human-like intelligent agents, with a particular focus on understanding and interpreting their behavior to enhance model control and optimize performance. While my prior work has predominantly been rooted in theoretical research, I am equally passionate about exploring the engineering aspects, aiming to bridge the gap between theoretical advancements and practical implementations to drive more robust, efficient, and human-aligned AI systems.

You can find my publications on <a href='https://scholar.google.com/citations?hl=en&user=f7KQvukAAAAJ'>Google Scholar <img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.

# 🔥 News
- *2024.02*: &nbsp;🎉 Our paper "When More is Less: Understanding Chain-of-Thought Length in LLMs" is now available on arXiv!
- *2024.02*: &nbsp;🎉 Our paper "A Theoretical Understanding of Self-Correction through In-context Alignment" has been accepted to NeurIPS 2024!
- *2024.02*: &nbsp;🏆 Best Paper Award at ICML 2024 Workshop on In-context Learning!

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint 2024</div><img src='images/cot_length.png' alt="cot_length" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[When More is Less: Understanding Chain-of-Thought Length in LLMs](https://arxiv.org/abs/2502.07266v1)

**Yuyang Wu\***, Yifei Wang\*, Tianqi Du, Stefanie Jegelka, Yisen Wang

[**Paper**](https://arxiv.org/abs/2502.07266v1)
- I mathematically model the CoT process as a task decomposition and subtask-solving procedure and demonstrate that a longer CoT is not necessarily better.
- Additionally, I conduct both synthetic and real-world experiments, revealing a U-shaped curve and the scaling behavior of the optimal CoT length.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='images/self_correction.png' alt="self_correction" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[A Theoretical Understanding of Self-Correction through In-context Alignment](https://openreview.net/pdf?id=OtvNLTWYww)

Yifei Wang\*, **Yuyang Wu\***, Zeming Wei, Stefanie Jegelka, Yisen Wang

[**Paper**](https://openreview.net/pdf?id=OtvNLTWYww)
- Best Paper Award at ICML 2024 Workshop on In-context Learning
- I established the first rigorous understanding of LLMs' self-correction ability and developed a simple and efficient self-correction algorithm (CaC) that shows significant improvements across different tasks.
</div>
</div>

# 🎖 Honors and Awards
- *2024.02* Best Paper Award at ICML 2024 Workshop on In-context Learning
- *2022* Silver Medal, Chinese Mathematical Olympiad

# 📖 Education
- *2022.09 - Present*, Undergraduate Student in Computer Science, Peking University

# 💻 Research Experience
- *2023.10 - Present*, Research Intern at ZERO Lab, Peking University
  - Researching the in-context abilities, including self-correction and chain-of-thought, in LLMs
  - Collaborating with Postdoc [Yifei Wang (MIT)](https://yifeiwang77.com) and advised by Prof. [Yisen Wang (PKU)](https://yisenwang.github.io)

# 💪 Skills
- **Programming Languages**: Python(proficient), C++(proficient), C#, Core Skills (Git/Linux/TeX/etc.)
- **Deep Learning Technologies**: Pytorch(proficient), CUDA parallel programming