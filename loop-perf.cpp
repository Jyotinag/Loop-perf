#include<bits/stdc++.h>

using namespace std;

void readConfig(){
    std::ifstream cFile ("config.txt");
    if(cFile.is_open())
    {
        std::string line;
        while(getline(cFile, line))
        {
            //line.erase(std::remove_if(line.begin(),line.end(), isspace)),line.end());
            if(line[0]=='#'|| line.empty())
                continue;
            auto delimiterPos = line.find("=");
            auto name = line.substr(0,delimiterPos);
            auto value = line.substr(delimiterPos + 1);
            std::cout << name <<" "<< value << '\n';
        }
    }
    else
    {
        std::cerr <<"Couldn't open config file for reading.\n";
    }
}

int main()
{
    readConfig();
    printf("Hello World\n");
    return 0;
}
