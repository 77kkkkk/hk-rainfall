import pandas as pd

# Step 1: Load the dataset into a pandas DataFrame
df = pd.read_csv('filtered_output.csv')

# Step 2: Combine Year, Month, and Day into a 'date' column
df['date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])

# Step 3: Convert the 'Value' column to numeric (handle 'Trace' as 0 or a small value)
df['Value'] = df['Value'].replace('Trace', 0).astype(float)

# Step 4: Filter the data to include only the years 2020-2024
df_filtered = df[df['date'].dt.year.between(2020, 2024)]

# Step 5: Remove negative or invalid rainfall values if any (optional)
df_filtered = df_filtered[df_filtered['Value'] >= 0]

# Step 6: Group by month and calculate the mean rainfall for each month
df_monthly_mean = df_filtered.groupby([df_filtered['date'].dt.month])['Value'].mean().reset_index()

# Step 7: Rename columns for easier understanding
df_monthly_mean.columns = ['Month', 'Mean Rainfall']

# Step 8: Print the results
print("Monthly Mean Rainfall (2020-2024):")
for index, row in df_monthly_mean.iterrows():
    print(f"Month: {row['Month']}, Mean Rainfall: {row['Mean Rainfall']:.2f} mm")

# Step 8: Create recommendations for each month based on the mean rainfall
recommendations = {
    1: "January: The weather in Hong Kong is cool and crisp, with almost no rain. It's the perfect time for a peaceful stroll through the city’s parks or a visit to the famous Victoria Peak, where the views are spectacular. January is also the month for Lunar New Year preparations. While the official celebrations usually begin in February, you can already feel the excitement in the air as the city gets ready for its grand festivities. If you’re into culture, you can enjoy the displays of intricate lanterns and start planning your shopping for the New Year. Perfect for those who prefer quieter days and crisp weather!",
    2: "February: February brings a little more rain, but it’s still fairly mild. The Lunar New Year usually falls in this month, and Hong Kong transforms into a festival wonderland. From street parades to fireworks, this is when the city really comes alive. Don't miss the spectacular Hong Kong Flower Market, where the scent of fresh blooms fills the air. While you're out celebrating, try the traditional Nian Gao (glutinous rice cake) – a sweet treat that symbolizes good luck and prosperity. If you're into cultural experiences, this is an unforgettable time to visit.",
    3: "March: March sees less rain, and with temperatures slowly warming up, it’s an excellent time to visit Hong Kong without the crowds. The city’s parks are blooming, and it’s the ideal moment for outdoor activities, like hiking the Dragon’s Back Trail or visiting the serene Nan Lian Garden. While you’re here, you might catch the Hong Kong Arts Festival, a celebration of music, theater, and dance. If you're looking for a mix of nature, culture, and fun, March is your month.",
    4: "April: April brings slightly more rain, but nothing too heavy. The weather is still quite pleasant for exploring, especially as the city starts gearing up for summer. If you're looking to dive into Hong Kong's local culture, April is a great time to experience the Ching Ming Festival, when people honor their ancestors by visiting tombs and enjoying family gatherings. It's a peaceful time in the city, with fewer tourists, making it the perfect moment to explore local temples and markets. Embrace the tradition and soak in the tranquility!",
    5: "May: May is when the rain starts picking up, but it’s also when the city begins to feel more tropical. The lush greenery around Hong Kong really comes to life. If you're in the mood for a more relaxed trip, head over to the beaches on Lantau Island, where you can escape the hustle and bustle. You might also experience the Buddha’s Birthday, which celebrates the birth of Lord Buddha. It’s a serene and spiritual time, with many locals visiting temples to offer prayers and gifts. Get ready for some rain, but also a lot of beauty and culture.",
    6: "June: June is one of the wettest months in Hong Kong, and it can be pretty humid. If you don’t mind the rain, this is an excellent time to visit indoor attractions like Hong Kong Museum of History or Ocean Park, an oceanarium and amusement park that’s fun for the whole family. June is also the month of the Dragon Boat Festival, celebrated with exciting boat races and delicious Zongzi (sticky rice dumplings wrapped in leaves). If you’re looking for a cultural and thrilling experience, this is your time!",
    7: "July: Welcome to the summer! July is hot and rainy, but that doesn’t stop Hong Kong from buzzing with energy. If you're an adventurer, the rain shouldn't stop you from exploring the city’s vibrant street food scene or hiking the lush trails. The Hong Kong International Film Festival often kicks off in July, so if you're a film lover, you’ll enjoy the screenings of global cinema. Don't forget to bring an umbrella, though! You’ll need it as the tropical storms are common during this month",
    8: "August: August is just as rainy and humid as July, but that doesn’t mean you can’t enjoy the city. If you don’t mind the weather, it’s a great time to visit the many museums and galleries that keep you cool while enriching your experience. Hong Kong also celebrates National Day on August 1st, with grand parades and fireworks lighting up the skyline. It’s a lively and exciting month for those who want to experience Hong Kong at its most vibrant and festive.",
    9: "September: September is the peak of the rainy season in Hong Kong, with heavy downpours and high humidity. It’s not the most ideal time for outdoor sightseeing, but it can be perfect for indoor explorations, like the Hong Kong Science Museum or a quiet afternoon at a local teahouse. On a brighter note, September is when the city celebrates Mid-Autumn Festival, where you can enjoy mooncakes and admire the lantern displays. If you’re okay with the wet weather, you’ll find a mix of cultural events and cool spots to unwind.",
    10: "October: October is a great month to visit Hong Kong! The weather is cooler, and the rainfall is minimal. It’s one of the best times of the year for sightseeing, with many tourists visiting iconic spots like Victoria Harbour or Tian Tan Buddha. This month also sees the Hong Kong Wine and Dine Festival, where food lovers can indulge in a diverse range of international cuisines. Perfect for outdoor activities and indulging in local delicacies!",
    11: "November: November is mild and relatively dry, making it another fantastic month for exploring the city. Take a walk through Hong Kong Disneyland, where the cooler temperatures make for a more comfortable experience. It’s also a great time to dive into Hong Kong’s local culture with the Hong Kong International Jazz Festival. The vibe is upbeat and festive, and you’ll feel the rhythm of the city with its vibrant music scene.",
    12: "December: December is one of the best times to visit Hong Kong. The weather is cool and dry, perfect for sightseeing, shopping, or enjoying a leisurely stroll through the city. It’s also a time for holiday festivities, with beautiful Christmas displays around Tsim Sha Tsui and Central. If you're into history and tradition, December is when The Winter Solstice is celebrated, an important time for family gatherings. The cool temperatures, paired with vibrant lights, make for an unforgettable experience."
}

# Step 9: Print the results with recommendations for each month
print("Monthly Mean Rainfall (2020-2024):")
for index, row in df_monthly_mean.iterrows():
    month_name = pd.to_datetime(f"{int(row['Month'])}/1/2024").strftime('%B')  # Get month name
    print(f"Month: {month_name}, Mean Rainfall: {row['Mean Rainfall']:.2f} mm - {recommendations[row['Month']]}")