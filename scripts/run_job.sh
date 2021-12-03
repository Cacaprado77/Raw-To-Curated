# COMANDO PARA CHAMAR O .SH
# chmod +x run_job.sh
# sudo ./run_job.sh

cd ..

make build

cd src && python3 read_write.py