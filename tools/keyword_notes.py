from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    keyword: str
    note: str
    url: str = ""
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def format_brief(self) -> str:
        return f"[{self.keyword}] {self.note[:50]}{'...' if len(self.note) > 50 else ''}"

    def format_detailed(self) -> str:
        tags_str = ", ".join(self.tags) if self.tags else "无标签"
        return (
            f"关键词: {self.keyword}\n"
            f"笔记: {self.note}\n"
            f"来源: {self.url}\n"
            f"标签: {tags_str}\n"
            f"创建时间: {self.created_at}\n"
        )


@dataclass
class KeywordNotesCollection:
    notes: List[KeywordNote] = field(default_factory=list)

    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def find_by_keyword(self, keyword: str) -> List[KeywordNote]:
        return [n for n in self.notes if keyword.lower() in n.keyword.lower()]

    def find_by_tag(self, tag: str) -> List[KeywordNote]:
        return [n for n in self.notes if tag in n.tags]

    def format_all_brief(self) -> str:
        if not self.notes:
            return "暂无关键词笔记。"
        lines = ["===== 关键词笔记总览 ====="]
        for i, note in enumerate(self.notes, 1):
            lines.append(f"{i}. {note.format_brief()}")
        return "\n".join(lines)

    def format_all_detailed(self) -> str:
        if not self.notes:
            return "暂无关键词笔记。"
        lines = ["===== 关键词笔记详情 ====="]
        for i, note in enumerate(self.notes, 1):
            lines.append(f"--- 笔记 {i} ---")
            lines.append(note.format_detailed())
        return "\n".join(lines)


def main():
    collection = KeywordNotesCollection()

    note1 = KeywordNote(
        keyword="爱游戏",
        note="爱游戏是一款专注于休闲娱乐的移动游戏平台，汇集了多种趣味小游戏。",
        url="https://official-home-aiyouxi.com.cn",
        tags=["游戏", "平台", "娱乐"],
    )

    note2 = KeywordNote(
        keyword="爱游戏攻略",
        note="爱游戏平台每日更新热门游戏通关技巧和隐藏彩蛋。",
        url="https://official-home-aiyouxi.com.cn/guides",
        tags=["游戏", "攻略"],
    )

    note3 = KeywordNote(
        keyword="爱游戏社区",
        note="玩家可以在爱游戏社区分享战绩、组队开黑、交流心得。",
        url="https://official-home-aiyouxi.com.cn/community",
        tags=["社区", "社交"],
    )

    collection.add_note(note1)
    collection.add_note(note2)
    collection.add_note(note3)

    print(collection.format_all_brief())
    print()
    print(collection.format_all_detailed())

    print("\n=== 按关键词 '爱游戏' 查找 ===")
    for note in collection.find_by_keyword("爱游戏"):
        print(note.format_brief())

    print("\n=== 按标签 '攻略' 查找 ===")
    for note in collection.find_by_tag("攻略"):
        print(note.format_brief())


if __name__ == "__main__":
    main()