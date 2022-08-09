// neko.cpp
# include <iostream>
# include <string>
using namespace std;

class Neko
{
private:
    string name;
public:
    Neko(string s){
        name = s;
    }
    void naku() const{
        cout << "I`m " << name << "!!" << endl;
    }
};

int main(){
    Neko dora("boss");
    cout << "create a cat named boss on your memory." << endl;
    cout << "boss said " << endl;
    dora.naku();
}