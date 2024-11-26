import json
import re
import copy

class CompanionIntercom:
    def sterilize_name(self, name):
        name = re.sub(r"\s", "_", name)
        name = name.lower()
        return name

    def createListenButton(self, page: int, pos: list):
        with open("templates/button_template_listen.json") as t:
            button = json.load(t)
        pos_x = pos[1]
        pos_y = pos[0]

        for i, b in enumerate(self.button_positions):
            f = {
                "id": "LriXVyti4LQxCBgMeKuuE",
                "action": "bank_current_step",
                "instance": "internal",
                "options": {
                    "location_target": "text",
                    "location_text": f"$(this:page)/{b[0]}/{b[1]}",
                    "location_expression": "concat($(this:page), '/', $(this:row), '/', $(this:column))",
                    "step_from_expression": False,
                    "step": 1,
                    "step_expression": "1",
                },
                "delay": 0,
            }
            button["steps"]["0"]["action_sets"]["up"].append(f)
            button["steps"]["0"]["action_sets"]["1000"].append(f)
            button["steps"]["0"]["action_sets"]["down"].append(copy.deepcopy(f))
            button["steps"]["0"]["action_sets"]["down"][i]["options"]["step"] = 3

        if page not in self.config["pages"]:
            self.config["pages"][page] = {}
        if "controls" not in self.config["pages"][page]:
            self.config["pages"][page]["controls"] = {}
        if pos_y not in self.config["pages"][page]["controls"]:
            self.config["pages"][page]["controls"][pos_y] = {}
        self.config["pages"][page]["controls"][pos_y][pos_x] = button

        return

    def createVolUpButton(self, page: int, pos: list):
        with open("templates/button_template_up.json") as f:
            button = json.load(f)

        pos_x = pos[1]
        pos_y = pos[0]

        for i, b in enumerate(self.button_positions):
            f = {
                "id": "LriXVyti4LQxCBgMeKuuE",
                "action": "bank_current_step",
                "instance": "internal",
                "options": {
                    "location_target": "text",
                    "location_text": f"$(this:page)/{b[0]}/{b[1]}",
                    "location_expression": "concat($(this:page), '/', $(this:row), '/', $(this:column))",
                    "step_from_expression": False,
                    "step": 1,
                    "step_expression": "1",
                },
                "delay": 0,
            }
            button["steps"]["0"]["action_sets"]["up"].append(f)
            button["steps"]["0"]["action_sets"]["1000"].append(f)
            button["steps"]["0"]["action_sets"]["down"].append(copy.deepcopy(f))
            button["steps"]["0"]["action_sets"]["down"][i]["options"]["step"] = 4

        if page not in self.config["pages"]:
            self.config["pages"][page] = {}
        if "controls" not in self.config["pages"][page]:
            self.config["pages"][page]["controls"] = {}
        if pos_y not in self.config["pages"][page]["controls"]:
            self.config["pages"][page]["controls"][pos_y] = {}
        self.config["pages"][page]["controls"][pos_y][pos_x] = button

        return

    def createVolDownButton(self, page: int, pos: list):
        with open("templates/button_template_down.json") as f:
            button = json.load(f)

        pos_x = pos[1]
        pos_y = pos[0]

        for i, b in enumerate(self.button_positions):
            f = {
                "id": "LriXVyti4LQxCBgMeKuuE",
                "action": "bank_current_step",
                "instance": "internal",
                "options": {
                    "location_target": "text",
                    "location_text": f"$(this:page)/{b[0]}/{b[1]}",
                    "location_expression": "concat($(this:page), '/', $(this:row), '/', $(this:column))",
                    "step_from_expression": False,
                    "step": 1,
                    "step_expression": "1",
                },
                "delay": 0,
            }
            button["steps"]["0"]["action_sets"]["up"].append(f)
            button["steps"]["0"]["action_sets"]["1000"].append(f)
            button["steps"]["0"]["action_sets"]["down"].append(copy.deepcopy(f))
            button["steps"]["0"]["action_sets"]["down"][i]["options"]["step"] = 5

        if page not in self.config["pages"]:
            self.config["pages"][page] = {}
        if "controls" not in self.config["pages"][page]:
            self.config["pages"][page]["controls"] = {}
        if pos_y not in self.config["pages"][page]["controls"]:
            self.config["pages"][page]["controls"][pos_y] = {}
        self.config["pages"][page]["controls"][pos_y][pos_x] = button

        return

    def createButton(self, name: str, page: int, pos: list, push_parameters: list, release_parameters: list, listen_endpoints: list=None, listen_volume_endpoints: list=None):
        with open("templates/button_template.json") as f:
            button = json.load(f)

        func_name = self.sterilize_name(name)
        pos_x = pos[1]
        pos_y = pos[0]
        vol_display_expr = f'($(internal:custom_listen_{func_name}_vol) == -20) ? "(min)" : ($(internal:custom_listen_{func_name}_vol) == 0) ? "(max)" : $(internal:custom_listen_{func_name}_vol)'

        button["style"]["text"] = name

        # Feedback "LISTEN"
        button["feedbacks"][0]["options"][
            "variable"
        ] = f"internal:custom_listen_{func_name}"
        # Feedback "LISTEN & PTT"
        button["feedbacks"][3]["children"][0]["options"][
            "variable"
        ] = f"internal:custom_listen_{func_name}"
        # Feedback "LISTEN & LATCH"
        button["feedbacks"][4]["children"][0]["options"][
            "variable"
        ] = f"internal:custom_listen_{func_name}"
        # Feedback "LISTEN_VOL display"
        button["feedbacks"][5]["style"][
            "text"
        ] = f'($(internal:custom_listen_{func_name}_vol) == -20) ? "(min)" : ($(internal:custom_listen_{func_name}_vol) == 0) ? "(max)" : $(internal:custom_listen_{func_name}_vol)'

        button["steps"]["2"]["action_sets"]["down"][0]["options"][
            "name"
        ] = f"listen_{func_name}"
        button["steps"]["2"]["action_sets"]["down"][0]["options"][
            "expression"
        ] = f"$(internal:custom_listen_{func_name}) * -1"

        # Step "vol_up"
        button["steps"]["3"]["action_sets"]["down"][0]["options"][
            "name"
        ] = f"listen_{func_name}_vol"
        button["steps"]["3"]["action_sets"]["down"][0]["options"][
            "expression"
        ] = f"($(internal:custom_listen_{func_name}_vol) < 0) ? $(internal:custom_listen_{func_name}_vol) + 2 : $(internal:custom_listen_{func_name}_vol)"

        # Step "vol_down"
        button["steps"]["4"]["action_sets"]["down"][0]["options"][
            "name"
        ] = f"listen_{func_name}_vol"
        button["steps"]["4"]["action_sets"]["down"][0]["options"][
            "expression"
        ] = f"($(internal:custom_listen_{func_name}_vol) > -20) ? $(internal:custom_listen_{func_name}_vol) - 2 : $(internal:custom_listen_{func_name}_vol)"

        for i, f in enumerate(push_parameters):
            par = f.split(" ")
            button["steps"]["0"]["action_sets"]["down"].append(
                {
                    "id": f"7NM5HkTz4kVAAFokJ77sO_{i}",
                    "action": "send_int",
                    "instance": "fk56I_UonwbLu1nOuArCJ",
                    "options": {"path": f"{par[0]}", "int": par[1]},
                    "delay": 0,
                    "disabled": False,
                }
            )

        for i, f in enumerate(release_parameters):
            par = f.split(" ")
            button["steps"]["0"]["action_sets"]["up"].append(
                {
                    "id": f"7NM5HkTz4kVAAFokJ77sO_{i}",
                    "action": "send_int",
                    "instance": "fk56I_UonwbLu1nOuArCJ",
                    "options": {"path": f"{par[0]}", "int": par[1]},
                    "delay": 0,
                    "disabled": False,
                }
            )
            button["steps"]["1"]["action_sets"]["down"].append(
                {
                    "id": f"7NM5HkTz4kVAAFokJ77sO_{i}",
                    "action": "send_int",
                    "instance": "fk56I_UonwbLu1nOuArCJ",
                    "options": {"path": f"{par[0]}", "int": par[1]},
                    "delay": 0,
                    "disabled": False,
                }
            )

        if listen_endpoints:
            self.button_positions.append(pos)
            if not listen_volume_endpoints:
                raise Exception(
                    "listen_volume_endpoints must be set when listen_endpoints is."
                )

            with open("templates/trigger_template.json") as f:
                trigger = json.load(f)
            self.config["triggers"] = {}
            key = f"Jf6n9QR9zfE9CzxwgKf_{func_name}"
            trigger["options"]["name"] = f"<LISTEN> {name}"
            trigger["events"][0]["options"][
                "variableId"
            ] = f"internal:custom_listen_{func_name}"
            for i, e in enumerate(listen_endpoints):
                trigger["action_sets"]["0"].append(
                    {
                        "id": f"dx3H5Xl56SX_C9CjEfUIc_{i}",
                        "action": "send_int",
                        "instance": "-uJM8ZoIPurpLZ1M--krT",
                        "options": {
                            "path": e,
                            "int": f"$(internal:custom_listen_{func_name}) == 1 ? 1 : 0",
                        },
                        "delay": 0,
                    }
                )
            self.config["triggers"][key] = copy.deepcopy(trigger)

            for i, e in enumerate(listen_volume_endpoints):
                button["steps"]["3"]["action_sets"]["down"].append(
                    {
                        "id": "1WHyJToPiTgmXRKqgyySB",
                        "action": "send_int",
                        "instance": "fk56I_UonwbLu1nOuArCJ",
                        "options": {
                            "path": e,
                            "int": f"$(internal:custom_listen_{func_name}_vol)",
                        },
                        "delay": 0,
                    }
                )
                button["steps"]["4"]["action_sets"]["down"].append(
                    {
                        "id": "1WHyJToPiTgmXRKqgyySB",
                        "action": "send_int",
                        "instance": "fk56I_UonwbLu1nOuArCJ",
                        "options": {
                            "path": e,
                            "int": f"$(internal:custom_listen_{func_name}_vol)",
                        },
                        "delay": 0,
                    }
                )

        self.createVariables(name)

        if page not in self.config["pages"]:
            self.config["pages"][page] = {}
        if "controls" not in self.config["pages"][page]:
            self.config["pages"][page]["controls"] = {}
        if pos_y not in self.config["pages"][page]["controls"]:
            self.config["pages"][page]["controls"][pos_y] = {}
        self.config["pages"][page]["controls"][pos_y][pos_x] = button

        return

    def createVariables(self, name):
        func_name = self.sterilize_name(name)
        self.config["custom_variables"][f"listen_{func_name}"] = {
            "description": "A custom variable",
            "defaultValue": "-1",
            "persistCurrentValue": False,
            "sortOrder": 4,
        }
        self.config["custom_variables"][f"listen_{func_name}_vol"] = {
            "description": "A custom variable",
            "defaultValue": "-6",
            "persistCurrentValue": False,
            "sortOrder": 5,
        }

        return

    def __init__(self):
        self.button_positions = []
        with open("templates/init.json") as f:
            self.config = json.load(f)

    def toJSON(self):
        return json.dumps(self.config, indent=2)
