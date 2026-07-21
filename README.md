# Assignment Writing Workflow

A personal Codex skill for managing university assignments from task interpretation to final checks.

这是一个个人课程作业流程 Skill。它会根据课程文件、rubric、任务类型和范例调整写作逻辑，并协助完成文献核查、大纲、中文工作稿、英文低改动、APA 7 和提交前检查。

## Features / 功能

- 读取课程大纲、作业要求、rubric 和教师范例
- 用中文解释作业要求并拆解评分标准
- 比较教师范例与外部可靠范例
- 根据任务类型生成本次写作逻辑
- 搜索、筛选和核查文献
- 核对 DOI 与文献信息是否对应
- 建立论点、证据、文献和 rubric 的对应关系
- 生成带文献位置的大纲
- 逐段生成和检查中文工作稿
- 对英文进行低改动检查
- 生成 APA 7 References list
- 检查格式、字数、引用和提交要求

## Supported Assignments / 支持类型

- Essay
- Literature review
- Research report
- Reflection
- Case study
- Proposal

每种类型会使用不同的范例、结构、证据规则和写作顺序。

## Installation / 安装

```bash
git clone https://github.com/lyz20070914lyz-boop/assignment-writing-workflow.git ~/.codex/skills/assignment-writing-workflow
```

安装后，在新的 Codex 对话中调用：

```text
使用 $assignment-writing-workflow，读取我的课程文件，开始这次作业。
```

然后提供课程大纲、作业要求、rubric 和已有范例。

## Workflow / 工作流程

1. 读取课程文件并确认任务要求
2. 判断作业类型
3. 比较教师范例和外部范例
4. 生成本次任务写作逻辑
5. 搜索并核查文献和 DOI
6. 筛选文献并建立证据对应关系
7. 生成大纲
8. 逐段完成中文工作稿
9. 执行英文低改动检查
10. 生成 APA 7 References
11. 完成格式和提交前检查

## Rules / 主要规则

- 不编造文献、DOI、研究结果、引用或课程要求
- 区分课程文件、外部信息、建议和假设
- 发现逻辑错误或信息不足时先指出问题
- 保留用户原意和非英语母语表达特征
- 低改动模式不重写整句或重组段落
- References 只包含正文实际引用的来源
- 不同任务类型使用不同写作逻辑

## Structure / 文件结构

```text
assignment-writing-workflow/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── evidence.md
│   ├── modes-applied.md
│   ├── modes-argumentative.md
│   ├── modes-empirical.md
│   ├── revision.md
│   └── workflow.md
└── scripts/
    └── validate_structure.py
```

## Validation / 检查

```bash
python3 scripts/validate_structure.py
```

The validator checks the skill structure, linked references, supported assignment types, and required workflow markers.
