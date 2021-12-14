class Record:
    def __init__(self, input_str: str, output_str: str):
        self.input_nums = Record.__convert_input_code(input_str)
        self.output_nums = Record.__convert_output_code(output_str)

    def __str__(self):
        return f"input numbers: {self.input_nums}, output numbers: {self.output_nums}"

    def get_input_nums(self):
        return self.input_nums

    def get_output_nums(self):
        return self.output_nums

    @staticmethod
    # after sort string cdfeb, cdfeb will become the same
    def __convert_input_code(input_str: str):
        tmp_nums = input_str.strip(" ").split(" ")
        for i in range(0, len(tmp_nums)):
            tmp_nums[i] = Record.__sort_code(tmp_nums[i])
        return tmp_nums

    @staticmethod
    # after sort string cdfeb, cdfeb will become the same
    def __convert_output_code(output_str: str):
        tmp_nums = output_str.strip(" ").split(" ")
        for i in range(0, len(tmp_nums)):
            tmp_nums[i] = Record.__sort_code(tmp_nums[i])
        return tmp_nums

    @staticmethod
    def __sort_code(code: str):
        res = ""
        tmp = []
        for char in code:
            tmp.append(char)
        tmp.sort()
        for c in tmp:
            res += c
        return res

    def determine_number(self,base_line):
        for num in self.input_nums:
            if len(num)==2:



 # base_line = {1: "cf",
                #              7: "acf",
                #              4: "bcdf",
                #              2: "acdeg", 3: "acdfg", 5: "abdfg",
                #              0: "abcefg", 6: "abdefg", 9: "abcdfg",
                #              8: "abcdefg"}