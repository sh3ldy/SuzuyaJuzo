import csv
domain_counts = {}

with open('out.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        email = row[2]
        domain = email.split('@')[-1]
        if domain in domain_counts:
            domain_counts[domain] += 1
        else:
            domain_counts[domain] = 1

sorted_domain_counts = sorted(domain_counts.items(), key=lambda x: x[1], reverse=True)

with open('domain_counts.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['domain', 'count'])
    for domain, count in sorted_domain_counts:
        writer.writerow([domain, count])
