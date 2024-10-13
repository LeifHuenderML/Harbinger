conda create -n harbinger python=3.9
conda activate harbinger
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
conda install numpy pandas scikit-learn matplotlib jupyter
conda install -c conda-forge tensorflow
conda install -c conda-forge keras
conda install -c conda-forge opencv
conda install conda-forge::polars
conda install conda-forge::plotly
pip install fastexcel