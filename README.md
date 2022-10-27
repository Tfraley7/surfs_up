## Surfs UP!
<br/>
<p align="center">Tyrone Fraley<br/>
UC Berkley Extension<br/>
August 31, 2022<br/>
<p/>
<br/>
<p align="center">
  <img width="460" height="200" src="Wave.jpeg">
</p>

## Overview 
Recently, I was on vacation in Hawaii. I discovered I had a passion for surfing during this trip and since then I have been planning to move to Hawaii. To do this I have been working on creaing a plan to move to Hawaii and start a business. The plan is to start a Surf and Shake shop that will serve surfboards and ice cream to customers. To accomplish this I will need to get an investor on board so I developed a solid business plan. However, once I did this and found an investor named W.Avy who is known for his love for surfing. W. Avy brought up a really good point to me - the weather in Hawaii. He later explained to me that he had a past venture (surf shop in Hawaii) and it was ultimately closed down due to weather conditions. He asked me if I could run some analytics from weather data he collected on every island in Hawaii. After analyzing the data and then discovering that Oahu would be the best place to start a business in Hawaii, W. Avy asked if I could drill down a bit more on Oahu. This time around he wanted to know about the temperature for the months of June and December to determine if the surf and ice cream business would be sustainable year-round.

## Results
The analysis was interesting, in that I could now see what the weather is like in Oahu year-round based on temperature. However, this was not envough - I also wanted to check out the percipitation during those months as well. The analysis for the temperature called for the following:<br/>
        <br/>
    * Analyze the temperatures for December.<br/>
            <br/>
        * December temp. deliverable code: december_temps_lst = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date)== 12).all()<br/>
                <br/>
    * Analyze the temperatures for June.<br/>
            <br/>
        * June temp. deliverable code: june_temps = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date) == 6).all()<br/>
                <br/>
    * Analyze the percipitation for June and December in 2017.<br/>
            <br/>
        * December prcp deliverable code: year_2017 = dt.date(2017, 12, 31) - dt.timedelta(days=365) | Dec_prcp_2017 = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_2017).filter(extract('month', Measurement.date)==12)<br/>
                <br/>
        * June prcp deliverable code: June_prcp_2017 = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_2017 ).filter(extract('month', Measurement.date)==6)<br/>
