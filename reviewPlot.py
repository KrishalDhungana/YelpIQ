import pandas as pd
from plotnine import *
import os

data = {
    'Average Review Count': [32.7086774235, 22.1282292156],
    'Average Stars': [3.69590903316, 3.5032879286],
    'Country': ['United States', 'Canada']
}
df = pd.DataFrame(data)
backgroundColour = "#ececec"
themeColour = "#3a3b3c"
chartTitle = "US vs Canada Business Review Metrics"

p = ggplot(data=df, mapping=aes(x='Country', y='Average Stars', fill='Country')) + \
    geom_bar(stat="identity", color="#ececec", size=0.25) + \
    geom_text(aes(label='Average Stars'), 
              va='bottom', 
              color = ['#779ecb', '#ff6961'],
              format_string="{:.2f}", 
              fontweight='bold',
              size=8, 
              nudge_y=0.02,) + \
    labs(x='Country', y='Average Stars', title='US vs Canada Business Review Metrics', subtitle='Average Star Rating') + \
    theme(axis_text_x=element_blank(),
          axis_text_y=element_text(color=themeColour,size=8),
          axis_title_y=element_text(color=themeColour,size=9),
          axis_title_x=element_blank(),
          plot_title=element_text(color=themeColour, size=20, face="bold", hjust=0.5),
          plot_subtitle=element_text(color=themeColour,size=10, hjust=0.5),
          panel_background=element_rect(fill=backgroundColour)) + \
    scale_fill_manual(values=['#ff6961', '#779ecb'])
outputFileName = "starRatingBar.png"
ggsave(p, filename=outputFileName, path=os.getcwd(), height=5, width=9, units='in', dpi=300) 

r = ggplot(data=df, mapping=aes(x='Country', y='Average Review Count', fill='Country')) + \
    geom_bar(stat="identity", color="#ececec", size=0.25) + \
    geom_text(aes(label='Average Review Count'), 
              va='bottom', 
              color = ['#779ecb', '#ff6961'],
              format_string="{:.2f}", 
              fontweight='bold',
              size=8, 
              nudge_y=0.02,) + \
    labs(x='Country', y='Average Review Count', title='US vs Canada Business Review Metrics', subtitle='Average Review Count') + \
    theme(axis_text_x=element_blank(),
          axis_text_y=element_text(color=themeColour,size=8),
          axis_title_y=element_text(color=themeColour,size=9),
          axis_title_x=element_blank(),
          plot_title=element_text(color=themeColour, size=20, face="bold", hjust=0.5),
          plot_subtitle=element_text(color=themeColour,size=10, hjust=0.5),
          panel_background=element_rect(fill=backgroundColour)) + \
    scale_fill_manual(values=['#ff6961', '#779ecb'])

outputFileName = "reviewCountBar.png"
ggsave(r, filename=outputFileName, path=os.getcwd(), height=5, width=9, units='in', dpi=300) 
