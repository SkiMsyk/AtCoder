// neko2.cpp
# include <iostream>
# include <string>
using namespace std;

class Neko
{
    private:
        string name;
    public:
        Neko(string s);
        void naku() const;
};

Neko::Neko(string s): name(s){}

void Neko::naku() const{
    cout << "I`m " << name << "!!" << endl;
}

int main(){
    string s;
    cout << "Let`s creating a cat, Please enter the name." << endl;
    cin >> s;

    Neko dora(s);
    cout << "Success!!" << endl;
    cout << "the cat said" << endl;

    dora.naku();
}