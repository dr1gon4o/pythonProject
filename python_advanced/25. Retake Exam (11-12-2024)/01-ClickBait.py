final_feed = []

suggested_links = list(map(int, input().split()))
featured_articles = list(map(int, input().split()))
target_engagement_value = int(input())

while suggested_links and featured_articles:

    suggested = suggested_links.pop(0)
    featured = featured_articles.pop()


    if suggested > featured:
        greater, smaller, origin = suggested, featured, "FIFO"
    elif featured > suggested:
        greater, smaller, origin = featured, suggested, "LIFO"
    else:
        final_feed.append(0)
        continue


    remainder = greater % smaller

    if origin == "LIFO":
        final_feed.append(remainder)
        if remainder != 0:
            featured_articles.append(remainder * 2)
    elif origin == "FIFO":
        final_feed.append(-remainder)
        if remainder != 0:
            suggested_links.append(remainder * 2)


total_engagement_value = sum(final_feed)


print("Final Feed:", ", ".join(map(str, final_feed)))


if total_engagement_value >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    shortfall = target_engagement_value - total_engagement_value
    print(f"Goal not achieved! Short by: {shortfall}")