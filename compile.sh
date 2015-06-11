if [ ! -d "./mupdf-1.6-source" ]; then
    tar -zxvf _install/mupdf-1.6-source.tar.gz -C ./
fi

cd mupdf-1.6-source
make
cd ../mupla
make
cd ../django_mupla/mupla_serve/mupla_cython
bash ./compile.sh
cd ../../..

if [ -e "./django_mupla/mupla_serve/mupla_cython/mupla_cython.so" ]
then
    echo "MuPla Compilation: Succeed"
else
    echo "MuPla Compilation: Failed"
fi

