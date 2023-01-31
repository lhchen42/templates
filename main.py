import os
import sys
from string import Template

def mock_forgery_data():
    return {
        "Type1":[
            ("Test1", "PASSED"),
            ("Test2", "Conditional"),
            ("Test3", "NotRelevant"),
            ("Test4", "Fail")
        ],
        "Type2": [
            ("Test1", "PASSED"),
            ("Test2", "PASSED"),
            ("Test3", "NotRelevant"),
            ("Test4", "NotRelevant")
        ]
    }

class StringTemplate:
    def __init__(self) -> None:
        pass

    @classmethod
    def read_template(cls, file: str) -> None:
        with open(file, "r") as f:
            return Template(f.read())

class PriotariesTemplate(StringTemplate):
    def __init__(self, data) -> None:
        super().__init__()
        self.data = data
    
    def _image_container():
        """
            <div class="ImagesContainer">
                {% if Image1 and not Image1.endswith("pdf") %} <img src='{{Image1}}' width="300"> {% else %} {% endif %}
                {% if Image2 and not Image2.endswith("pdf") %} <img src='{{Image2}}' width="300"> {% else %} {% endif %}
                {% if Image3 %} <img src='{{Image3}}' width="300"> {% else %} {% endif %}
                {% if Image4 %} <img src='{{Image4}}' width="300"> {% else %} {% endif %}
                <br>
            </div>
        """

        div_s = "<div class=\"ImagesContainer\">"
        
        div_e = "</div>"
        
    def Forgerys(self, ForgeryTests):
        """
                {% for type in ForgeryTestsOrder %}
                <h2>Forgery - {{ type }}</h2>
                    {% if ForgeryTests[type] == [] %}
                        <span>No tests for this forgery type</span>
                    {% else %}
                        <div class="HorizontalList">
                            {% for item in ForgeryTests[type] %}
                                <div class="TestItem 
                                    {% if item[1] == 'PASSED' %} 
                                        green-back-light 
                                    {% elif item[1] == 'Conditional' %}
                                        orange-back
                                    {% elif item[1] == 'NotRelevant' %}
                                        grey-back
                                    {% else %} 
                                        red-back 
                                    {% endif %}"
                                >
                                    <div class="TestResult" style="font-size: 12pt;">
                                        <!-- <span style="color: green;">&#9745</span> -->
                                        {% if item[1] == 'PASSED' %}
                                            <span>&#9745</span>
                                        {% elif item[1] == 'Conditional' %}
                                            <span>!</span>
                                        {% elif item[1] == 'NotRelevant' %}
                                            <span>?</span>
                                        {% else %}
                                            <span>&#9746</span>
                                        {% endif %}
                                    </div>
                                    <div class="TestType">
                                        {{item[0]}}
                                    </div>
                                </div>
                            {% endfor %}
                        </div>
                    {% endif %}
                {% endfor %}
            """

        if ForgeryTests == []:
            return "<span>No tests for this forgery type</span>"
        else:
            t = StringTemplate.read_template("templates\\forgery_t.html")
            
            its=""
            for item in ForgeryTests:
                forgery_item_t = """
                        <div class="TestItem $color">
                            <div class="TestResult" style="font-size: 12pt;">
                                <!-- <span style="color: green;">&#9745</span> -->
                                $prefix
                            </div>
                            <div class="TestType">
                                $type
                            </div>
                        </div>
                        """
                it = Template(forgery_item_t).safe_substitute(
                    color=self._get_color(item[1]), prefix=self._get_prefix(item[1]), type=item[0])
                its+=it
            return t.safe_substitute(content=its)
                
                

    def _get_color(self, item):
        if item == 'PASSED':
            return 'green-back-light '
        elif item == 'Conditional':
            return 'orange-back'
        elif item == 'NotRelevant':
            return 'grey-back'
        else:
            return 'red-back'

    def _get_prefix(self, item):
        if item == 'PASSED':
            return '<span>&#9745</span>'
        elif item == 'Conditional':
            return '<span>!</span>'
        elif item == 'NotRelevant':
            return '<span>?</span>'
        else:
            return '<span>&#9746</span>'


if __name__ == "__main__":
    print("Hello World")
    t1_p = os.path.join("./templates", "t1.html")
    st = StringTemplate.read_template(t1_p)
    # print(st.safe_substitute(title="String Template"))

    A = PriotariesTemplate({})
    forgery_results = ""
    for type in mock_forgery_data():
        forgery_result = A.Forgerys(mock_forgery_data()[type])
        forgery_results+=forgery_result
    # forgery_result = A.Forgerys(mock_forgery_data()["Type1"])
    result = st.safe_substitute(title="String Template", image_container="", foregery_tests=forgery_results)

    with open("result.html", "w") as f:
        f.write(result)



