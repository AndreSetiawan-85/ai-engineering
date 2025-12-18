Capstone Project Module 02 - Travel Insurance Claim Prediction
File : Capstone_Project_Module_02.ipynb

Tujuan : membangun model machine learning yang mampu memprediksi kemungkinan seorang penumpang untuk melakukan claim travel insurance.

Dataset : data_travel_insurance.csv (sumber : Purwadhika Digital School)
Target : Claim
0 = tidak claim
1 = claim

Langkah-langkah pengerjaan
1. Data cleaning
   - Cek missing value --> drop kolom Gender yang memiliki banyak missing value 
   - Cek duplicate data --> drop duplicate data
   - Cek outlier --> disesuaikan datanya dengan menggunakan negative value & log transformation, IQR Capping (Winsorizing)
2. Correlation Matrix
3. Bar Plot Claim Rate
4. Grouping value di kolom Destination berdasarkan wilayah
5. Train Test Data Split
6. Encoding untuk data kategorikal
7. SMOTE Resampling --> untuk mengatasi imbalance dataset
8. Model Selection : Random Forest Classifier
9. Threshold tuning --> penyesuaian threshold agar model mampu memprediksi kelas minoritas (claim=yes)
10. Evaluation Metric (fokus ke nilai recall tertinggi untuk meminimalkan resiko claim yang tidak terdeteksi)
11. Bandingkan hasil training data test dengan data train
12. Hyperparameter Tuning
13. Threshold tuning setelah proses Hyperparameter Tuning
14. Save model --> agar model tidak perlu ditraining lagi saat digunakan kembali
15. Conclusion
16. Recommendation 
