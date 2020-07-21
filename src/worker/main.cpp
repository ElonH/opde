#include "worker.h"
#include <fstream>
#include <iostream>
#include <sstream>

int main(int argc, char **argv)
{
    if (argc < 3)
    {
        std::cerr << "Please provide input and output path" << std::endl;
        return 1;
    }
    std::ifstream ifs(argv[1]);
    auto data = std::string((std::istreambuf_iterator<char>(ifs)),
                            (std::istreambuf_iterator<char>()));
    ifs.close();
    auto ans = BuildWorkerPyramid(data);
    std::ofstream ofs(argv[2]);
    ofs << ans;
    ofs.close();
    return 0;
}
