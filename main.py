import pandas as pd
from utils import extract_root_domain


def main():

    # read data
    awards = pd.read_csv('recruitment - awards.csv')
    emails = pd.read_csv('recruitment - emails.csv')
    
    # clean and transform data
    awards['Domain'] = awards['url'].apply(extract_root_domain)
    emails['Domain'] = emails['Domain'].str.lower()
    
    # merge data (left join)
    merged_df = emails.merge(awards, on='Domain', how='left')
    
    # save to csv (final result)
    merged_df.to_csv('emails - awards (full).csv', index=False)
    
    print('Done!')

if __name__ == "__main__":
    main()
