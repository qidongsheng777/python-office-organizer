# Python Office Organizer

一个轻量级办公自动化小工具，用于批量整理文件并汇总 CSV/Excel 表格信息。项目适合日常学习资料、课程文件、表格台账等场景，目标是减少重复的手工分类、复制和统计工作。

## 功能

- 按文件类型自动分类：文档、表格、图片、压缩包、其他文件。
- 可按修改月份继续分组，方便整理阶段性资料。
- 可按关键词创建额外分类文件夹。
- 批量读取 CSV 和 Excel 文件，生成统一的汇总表。
- 对表格行数、列数、空单元格数量和表头字段进行统计。

## 安装

```bash
python -m pip install -r requirements.txt
```

## 使用示例

整理文件：

```bash
python -m office_organizer.cli organize examples/input_files output/organized --by-date --keyword resume
```

汇总表格：

```bash
python -m office_organizer.cli summarize examples/tables output/table_summary.csv
```

## 项目结构

```text
office_organizer/
  cli.py             命令行入口
  organizer.py       文件分类整理逻辑
  table_summary.py   CSV/Excel 汇总逻辑
examples/            示例输入文件
tests/               基础测试
```

## 简历表述参考

项目名称：基于 Python 的文件与表格自动化整理工具

技术方向：Python、文件批量处理、Excel 数据整理、办公自动化

- 情境：在日常学习和资料整理过程中，经常需要对大量文件和表格数据进行分类、筛选和汇总，手工处理效率低且容易出错。
- 任务：设计并实现一个 Python 自动化整理工具，用于完成文件批量分类、表格数据读取、关键信息筛选和结果汇总。
- 行动：使用 Python 编写脚本，按文件类型、日期和关键词对文件进行自动归类；读取 CSV/Excel 表格并提取关键信息，生成统一格式的汇总结果；针对空字段等情况加入基础检查提示。
- 结果：完成文件整理与表格汇总的自动化流程，减少重复手工操作，提高资料整理效率，并加深了对 Python 文件处理、表格处理和自动化办公场景的理解。
