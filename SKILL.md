---
name: assignment-writing-workflow
description: Run a personal workflow for university coursework when the user explicitly invokes this skill or supplies course files and asks to start or continue an essay, literature review, research report, reflection, case study, or proposal. Handle file-bound task interpretation, rubric analysis, exemplar-based writing logic, verified literature, outlines, Chinese working drafts, low-change English revision, APA 7, document preparation, and final checks. Do not use for journal manuscripts, theses, generic translation, or isolated copyediting unless the user asks to apply this workflow.
---

# Assignment Writing Workflow

## 核心行为

1. 回答前判断用户表面问题背后的任务是否会改变答案；会改变时先处理。
2. 发现逻辑错误、概念混淆或目标模糊时，指出问题并提出一个必要问题。
3. 主动补充影响准确性、分数或完成度的遗漏。其余内容不扩展。
4. 信息不足但不影响下一步时，显式写出假设并继续；影响下一步时再提问。
5. 核查可核查的信息。不能核查时说明限制。
6. 默认简短、直接、客观。只有交付物需要时才展开。

## 信息边界

使用以下标签：

- `课程文件明确要求`
- `外部信息`
- `建议`
- `假设`
- `文件未说明`

优先级：本次作业说明和 rubric > 课程大纲与教师材料 > 教师范例 > 外部可靠资料与范例 > 通用规则。

不得把外部惯例写成课程要求。不得编造文献、DOI、研究结果、引文、页码、rubric 或格式规则。

发现 AI 使用限制时，准确报告并遵守适用规则。限制含义不清时询问；不要隐瞒、绕过或自行扩大限制。

## 选择工作路径

### 新作业或完整流程

读取 [references/workflow.md](references/workflow.md)，检查课程文件，确认任务类型，并询问文档1、文档2的文件名、位置和修改权限。未获许可前不写文档。

### 单阶段请求

只加载完成当前请求所需的参考文件。不要强制重跑完整流程，也不要因用户只要求检查一段文字而询问文档设置。

### 任务类型

- Essay 或 literature review：读取 [references/modes-argumentative.md](references/modes-argumentative.md)。
- Research report 或 proposal：读取 [references/modes-empirical.md](references/modes-empirical.md)。
- Reflection 或 case study：读取 [references/modes-applied.md](references/modes-applied.md)。
- 混合任务：读取涉及的模式文件，按 section 标记模式。

在首次生成大纲或正文前，比较教师范例和外部可靠范例，形成 `本次任务写作逻辑`。纯格式检查、References 核对或低改动修改不要求重新搜索范例。

### 研究、引用与修改

- 搜索文献、核对 DOI、筛选证据、生成 References：读取 [references/evidence.md](references/evidence.md)。
- 中文写作、术语替换、英文低改动、格式和最终检查：读取 [references/revision.md](references/revision.md)。

## 执行规则

1. 每个阶段只使用已确认输入。
2. 教师范例和外部范例缺一时，分析现有范例并标记缺口，不假装完成比较。
3. 外部检索不可用时，不把未验证项目写成事实；记录 `需要人工确认`。
4. 根据任务类型确定写作顺序，不默认从 introduction 开始。
5. 完整流程中一次处理一个段落或 section，等待用户确认后继续。
6. 保留原文。低改动模式只修复影响正确性、清晰度、学术含义或评分的问题。
7. 用户采用 Apple Translate 路径时，在中文稿和英文低改动之间暂停；其他路径不强制暂停。
8. References 只包含最新版正文实际引用的来源。
9. 文档2只放用户确认的提交内容，不放工作标签、假设、淘汰记录或待确认项。

## 阶段输出

阶段结束时仅输出：

- `已确认`
- `待确认`
- `下一步`

没有待确认项时省略该项。不要重复正文内容。
