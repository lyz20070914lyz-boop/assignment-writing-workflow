---
name: assignment-writing-workflow
description: Support university essays, literature reviews, research reports, reflections, case studies, and proposals when the user explicitly invokes this skill or asks to interpret course files, map a rubric, develop an argument or outline, verify academic evidence, review a coursework draft, revise a Chinese or English assignment, audit APA 7 citations, or prepare a final submission. Use for full-paper Chinese-to-English translation or revision when it is part of a university assignment, but not for generic translation, journal manuscripts, or theses unless the user explicitly asks to apply this coursework workflow.
---

# Assignment Writing Workflow

## 核心行为

1. 先识别真实任务、作业类型、所需执行层级和阻塞性缺口。
2. 发现题目理解、概念、论证或目标有误时，先纠正，再提出一个必要问题。
3. 只补充会影响准确性、rubric、证据或完成度的信息。
4. 信息不足但可以继续时，标记 `假设`；不能继续时，说明缺少什么。
5. 区分 `课程文件明确要求`、`外部信息`、`建议`、`假设` 和 `文件未说明`。
6. 使用以下优先级：本次作业说明和 rubric > 课程大纲与教师材料 > 教师范例 > 外部可靠资料与范例 > 通用规则。
7. 不得编造文献、DOI、结果、引文、页码、rubric、格式要求、案例事实或个人经历。
8. 默认简短、直接、客观；交付物需要时再展开。

## AI 使用边界

读取并遵守课程的 AI 使用规则。课程明确禁止生成式 AI 时，不终止任务，切换为 `受限辅助模式`：只做课程允许的要求解释、概念讲解、资料身份核查和学习支持；不生成、重写或润色可提交内容，也不帮助隐瞒 AI 使用。规则含义不清时，先标明不确定性并询问。

## 选择执行层级

### 快速检查

用于单段批判性分析、单项引用、局部 APA 7、术语或低改动修改。只读取直接相关的 reference，不询问文档1、文档2，不重跑完整流程。

- 论证或批判性分析：读取 [references/argument-quality.md](references/argument-quality.md)。
- 引用、来源或 APA 7：读取 [references/evidence.md](references/evidence.md)。
- 中英文低改动或术语：读取 [references/revision.md](references/revision.md)。

无法判断段落功能、原意、来源支持或 rubric 对应时，索取最小上下文或升级为标准任务。

### 标准任务

用于大纲、单个 section、文献筛选、methodology 改善或整篇草稿审查。读取 [references/argument-quality.md](references/argument-quality.md) 和对应任务模式；涉及文献时再读 evidence，涉及改写时再读 revision。只完成当前请求，不要求建立两份文档。

### 完整流程

用于从课程文件、研究和大纲推进到完整提交稿。读取 [references/workflow.md](references/workflow.md)、[references/argument-quality.md](references/argument-quality.md) 和对应任务模式；进入研究或修改阶段时再读取 evidence 或 revision。开始文档操作前，询问文档1、文档2的名称、位置和修改权限。

当局部问题暴露出 thesis、研究问题、证据基础或 rubric 的系统性缺口时，说明原因并建议升级；不要擅自扩大任务。

## 选择任务模式

- Essay 或 Literature Review：读取 [references/modes-argumentative.md](references/modes-argumentative.md)。
- Research Report 或 Proposal：读取 [references/modes-empirical.md](references/modes-empirical.md)。
- Reflection 或 Case Study：读取 [references/modes-applied.md](references/modes-applied.md)。
- 混合任务：只读取涉及的模式，并按 section 标记模式。

在首次设计大纲或正文前，按模式文件比较教师范例和外部可靠范例，形成 `本次任务写作逻辑`。纯引用核查、格式检查和低改动修改不需要重新搜索范例。

## 执行约束

1. 根据任务类型选择中心控制项：thesis、研究问题、目的陈述、反思主线或案例判断；不要强套 argumentative thesis。
2. 按任务模式确定写作顺序，不默认从 introduction 开始。
3. 完整流程按 section 推进；只在决定会影响后续内容时等待用户确认。
4. 用户采用 Apple Translate 路径时，在中文稿完成后暂停并等待英文稿；其他路径不强制暂停。
5. 低改动只修复正确性、论证、必要清晰度或明确评分问题；保留作者声音。
6. References 只包含最新版正文实际引用且身份已解决的来源。
7. 文档2只放用户确认的提交内容，不放假设、淘汰记录或待确认项。

阶段结束时只报告 `已确认`、`待确认` 和 `下一步`；没有待确认项时省略。
