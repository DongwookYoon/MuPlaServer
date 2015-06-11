if [ -d "./mupdf-1.6-source" ]; then
    cd mupdf-1.6-source
    make clean
    cd ..
fi

cd mupla
make clean

cd ../django_mupla/mupla_serve/mupla_cython
bash clean.sh
cd ../../..
