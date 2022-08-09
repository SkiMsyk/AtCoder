// ex7.cpp
# include <iostream>
# include <string>
using namespace std;

class Rocket
{
    private:
        int nenryo;
        int sokudo;
    
    public:
        Rocket(int);
        void kasoku();
};

// definition of constructor
Rocket::Rocket(int x): nenryo(x), sokudo(0){}

// definition of kasoku function
void Rocket::kasoku()
{
    if(nenryo >= 2){
        sokudo += 2;
        nenryo -= 2;
        cout << "nenryo is " << nenryo << " now" << endl;
        cout << "sokudo is " << sokudo << " now" << endl;
    }
    else{
        cout << "you have no nenryo for kasoku, sorry." << endl;
    }
}

int main()
{
    cout << "creating Rocket on your memory" << endl;
    int n;
    cout << "Please enter the initial nenryo amount.";
    cin >> n;

    Rocket ohtori(n);

    cout << "acceleration" << endl;
    ohtori.kasoku();
    cout << "acceleration again" << endl;
    ohtori.kasoku();
    cout << "end the trip" << endl;
}