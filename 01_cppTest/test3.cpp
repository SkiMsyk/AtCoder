# include <iostream>
# include <string>
using namespace std;

int main(){
    // declaration
    int age;
    string name;

    cout << "Please tell me your name" << endl;
    cin >> name;
    cout << name << ", welcome!!" << endl;

    cout << "Please tell me your age" << endl;
    cin >> age;
    cout << "Thanks, your name is " << name << ", and your age is " << age << endl;
}