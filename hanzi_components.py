import json


class HanziComponents:

    _components = {}

    def __init__(self):
        with open("hanzi_components.jsonl", "r", encoding="utf-8") as f:
            for line in f:
                buffer = json.loads(line)
                character = buffer["character"]
                self._components[character] = []
                if "components1" in buffer:
                    self._components[character].append(buffer["components1"])
                if "components2" in buffer:
                    self._components[character].append(buffer["components2"])
                if "components3" in buffer:
                    self._components[character].append(buffer["components3"])

    def components(self, hanzi, level=1):
        if len(hanzi) > 1:
            print(f'不支持多字查询。')
            return
        if hanzi not in self._components:
            print(f'【{hanzi}】不在数据集中。')
            return []
        assert level > 0
        if level > len(self._components[hanzi]):
            print(f'【{hanzi}】不支持查询第 {level} 级。')
            return []
        return self._components[hanzi][level-1]
