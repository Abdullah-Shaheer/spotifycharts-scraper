import requests
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://charts.spotify.com/',
    'content-type': 'application/json',
    'spotify-app-version': '0.0.0.production',
    'app-platform': 'Browser',
    'Origin': 'https://charts.spotify.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Priority': 'u=4',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get('https://charts-spotify-com-service.spotify.com/public/v0/charts', headers=headers)
data = response.json()
# print(data)
views = data.get("chartEntryViewResponses")

tracks_data = []
highlights_songs = []
albums_data = []
highlights_albums = []
artists_data = []
highlights_artists = []

title_tracks = 'Weekly Top Songs: Global'
title_albums = 'Weekly Top Albums: Global'
title_artists = 'Weekly Top Artists: Global'

for view in views:
    title = view.get('displayChart').get('chartMetadata').get('readableTitle')
    if title == title_tracks:
        print("Scraping data")
        entries = view.get("entries")
        highlights = view.get("highlights")
        for highlight in highlights:
            streak_type = highlight.get('type')
            text = highlight.get('text')
            image_highlight_url = highlight.get("displayImageUri")
            highlights_songs.append({'Streak': streak_type,
                                     'Details': text,
                                     'Image_url': image_highlight_url})
        for entry in entries:
            chart_data = entry.get("chartEntryData")
            current_rank = chart_data.get('currentRank')
            previousRank = chart_data.get("previousRank")
            track_meta = entry.get("trackMetadata")
            track_name = track_meta.get('trackName')
            track_url = track_meta.get('trackUri')
            image_url = track_meta.get("displayImageUri")
            artists = track_meta.get('artists')
            # print(type(artists))
            # artist_name = artists.
            # artists_spotify = artists["spotifyUri"]
            for artist in artists:
                artist_name = artist.get('name')
                artist_spotify = artist.get('spotifyUri')
                # artists_track_data.append({'Artist Name': artist_name,
                #                            'Artist Spotify': artist_spotify})
            tracks_data.append({'Name': track_name,
                                'Rank': current_rank,
                                'Previous Rank': previousRank,
                                'Image URL': image_url,
                                'Song URL': track_url,
                                'Artist/s Name': artist_name,
                                'Artist Spotify': artist_spotify})
        # tracks_data.extend(artists_track_data)
        df = pd.DataFrame(tracks_data)
        df.to_excel('Top_Global_Songs.xlsx', index=False)
        df.to_csv('Top_Global_Songs.csv', index=False)
        df1 = pd.DataFrame(highlights_songs)
        df1.to_excel('Top_Global_Songs_Highlights.xlsx', index=False)
        df1.to_csv('Top_Global_Songs_Highlights.csv', index=False)

    elif title == title_albums:
        entries1 = view.get('entries')
        if not entries1:
            print('There are no entries1')
        highlights1 = view.get("highlights")
        for highlight in highlights1:
            streak_type = highlight.get('type')
            text = highlight.get('text')
            image_highlight_url = highlight.get("displayImageUri")
            highlights_albums.append({'Streak': streak_type,
                                      'Details': text,
                                      'Image_url': image_highlight_url})

        for entry1 in entries1:
            current_rank_1 = entry1.get('chartEntryData').get('currentRank')
            previous_rank_1 = entry1.get('chartEntryData').get('previousRank')
            album_meta_data = entry1.get('albumMetadata')
            album_name = album_meta_data.get('albumName')
            album_url = album_meta_data.get('albumUri')
            album_image_url = album_meta_data.get('displayImageUri')
            artists1 = album_meta_data.get('artists')
            for artist1 in artists1:
                artist1_name = artist1.get('name')
                artist1_spotify = artist1.get('spotifyUri')
            albums_data.append({'Name': album_name,
                                'Rank': current_rank_1,
                                'Previous Rank': previous_rank_1,
                                'Image URL': album_image_url,
                                'Song URL': album_url,
                                'Artist/s Name': artist1_name,
                                'Artist Spotify': artist1_spotify})

        df2 = pd.DataFrame(albums_data)
        df2.to_excel('Top_Global_Albums.xlsx', index=False)
        df2.to_csv('Top_Global_Songs_Highlights.csv', index=False)
        df3 = pd.DataFrame(highlights_albums)
        df3.to_excel('Top_Global_Albums_Highlights.xlsx', index=False)
        df3.to_csv('Top_Global_Songs_Highlights.csv', index=False)

    elif title == title_artists:
        entries = view.get("entries")
        highlights = view.get("highlights")
        for highlight in highlights:
            streak_type = highlight.get('type')
            text = highlight.get('text')
            image_highlight_url = highlight.get("displayImageUri")
            highlights_artists.append({'Streak': streak_type,
                                       'Details': text,
                                       'Image_url': image_highlight_url})
        for entry in entries:
            chart_data = entry.get("chartEntryData")
            current_rank = chart_data.get('currentRank')
            previousRank = chart_data.get("previousRank")
            track_meta = entry.get("artistMetadata")
            track_name = track_meta.get('artistName')
            track_url = track_meta.get('artistUri')
            image_url = track_meta.get("displayImageUri")
            artists = track_meta.get('artist')
            artists_data.append({'Name': track_name,
                                 'Rank': current_rank,
                                 'Previous Rank': previousRank,
                                 'Artist URL': track_url,
                                 'Photo URL': image_url})
        df4 = pd.DataFrame(artists_data)
        df4.to_excel('Top_Global_Artists.xlsx', index=False)
        df4.to_csv('Top_Global_Songs_Highlights.csv', index=False)
        df8 = pd.DataFrame(highlights_artists)
        df8.to_excel('Top_Global_Artists_Highlights.xlsx', index=False)
        df8.to_csv('Top_Global_Songs_Highlights.csv', index=False)
print('Scraped the top songs, top albums, and top artists of the week on spotify charts!')
