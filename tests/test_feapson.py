import unittest

import feapson


class MyTestCase(unittest.TestCase):
    def test_dumps_dict(self):
        data = {"a": True, "c": False, "b": '{"a": true}'}
        result = feapson.dumps(data, indent=4, ensure_ascii=False)

        self.assertEqual(
            result,
            r"""{
    "a": True,
    "c": False,
    "b": "{\"a\": true}"
}""",
        )

    def test_dumps_dict2(self):
        data = {"a": True, "c": False, "b": '{"a": true}'}
        result = feapson.dumps(data)

        self.assertEqual(
            result,
            r'{"a": True, "c": False, "b": "{\"a\": true}"}'
        )

    def test_loads_dict(self):
        data_str = '{"a": True,"c": False, "b": "{\\"a\\": true}"}'
        result = feapson.loads(data_str)
        self.assertEqual(result, {"a": True, "c": False, "b": '{"a": true}'})

    def test_loads_json(self):
        data_str = '{"a": true,"c": false, "b": "{\\"a\\": true}"}'
        result = feapson.loads(data_str)
        self.assertEqual(result, {"a": True, "c": False, "b": '{"a": true}'})


if __name__ == "__main__":
    unittest.main()
