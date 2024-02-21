# Loading the correct libraries and packages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pdf
import seaborn as sns

# Feeding in the data
df = pd.read_excel("Aussiesharks.xlsx")
print(df.head())
print(df.dtypes)

# Creating a PDF file to save the report
with pdf.PdfPages("Shark_Incidents_Report.pdf") as pdf_report:
    # Trend Analysis over Time: Visualize the trend of shark incidents over the years.
    plt.figure(figsize=(10, 6))
    trend_over_time = df.groupby(['Incident.year']).size()
    trend_over_time.plot(kind='line', color='blue')
    plt.title('Trend of Shark Incidents in Australia (1791-2022)')
    plt.xlabel('Year')
    plt.ylabel('Number of Incidents')
    plt.grid(True)
    pdf_report.savefig()
    plt.close()

    # Geographical Distribution: Plot the geographical distribution of shark incidents.
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Longitude', y='Latitude', hue='State', palette='viridis', alpha=0.7)
    plt.title('Geographical Distribution of Shark Incidents by State')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend(title='State')
    pdf_report.savefig()
    plt.close()

    # Injury Severity Analysis: Visualize the distribution of injury severity.
    plt.figure(figsize=(8, 6))
    df['Injury.severity'].value_counts().plot(kind='bar', color='green')
    plt.title('Distribution of Injury Severity in Shark Incidents')
    plt.xlabel('Injury Severity')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    pdf_report.savefig()
    plt.close()

    # Victim Demographics: Explore victim demographics such as gender and age.
    plt.figure(figsize=(10, 6))
    df['Victim.gender'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightgreen'])
    plt.title('Distribution of Victim Gender in Shark Incidents')
    plt.axis('equal')
    pdf_report.savefig()
    plt.close()

    # Environmental Factors: Analyze environmental factors like water temperature and air temperature.
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Water.temperature.°C'], df['Air.temperature.°C'], color='orange', alpha=0.5)
    plt.title('Relationship between Water and Air Temperature')
    plt.xlabel('Water Temperature (°C)')
    plt.ylabel('Air Temperature (°C)')
    plt.grid(True)
    pdf_report.savefig()
    plt.close()

    # Safety Measures Effectiveness: Evaluate the effectiveness of safety measures and deterrents.
    plt.figure(figsize=(10, 6))
    df['Deterrent.brand.and.type'].value_counts().plot(kind='barh', color='purple')
    plt.title('Distribution of Deterrent Brands and Types')
    plt.xlabel('Count')
    plt.ylabel('Deterrent Brand and Type')
    plt.grid(axis='x')
    pdf_report.savefig()
    plt.close()

print("PDF report generated successfully!")
