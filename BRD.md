Business Requirements

Project Title: Oreo Flavor Recommendation 
By: Cody Riley


Summary: To identify a potential new flavor concept for Oreo, I analyzed and reviewed social media data across 14 existing flavors and evaluated 4 proposed concepts using a Python composite scoring model. "Oreo Milkshake" emerged as the top recommendation with a 0.993 composite score, making it the best candidate for a limited-edition launch.

Goals:
    Find a flavor concept that resonates with college-aged and young adult demographics (18–24).

    Drive social media engagement during a limited-time promotional window.

    Test if dessert concepts generate enough interest to warrant future releases.

Project Scope:
    In-Scope: Data analysis, flavor selection, basic packaging ideas, and U.S. market recommendations.

    Out-of-Scope: International distribution, manufacturing logistics, or dietary-specific variations (ex: gluten-free options).

Production Requirements:
    Product Design: White chocolate cookie paired with a vanilla and chocolate fudge swirl crème filling.

    Packaging: Standard 12.2 oz pack with a "Limited Edition" banner and a QR code linking to a feedback survey.

    Feedback Loop: Simple tracking system to capture post-launch ratings and consumer sentiment.

Target Metrics:
    Sales Rate: Sell through 80% of initial store inventory within 6 weeks of launch.

    Social Sentiment: Positive feedback at or above 75% during the promotional push.

Risks:
    Risk: Consumers might think "Oreo Milkshake" sounds like a revamped standard Oreo.
        Solution: Focus marketing on the "dessert milkshake" theme and highlight the dual-crème layer.

    Risk: Stockouts if initial demand spikes higher than expected.
        Solution: Partner with backup ingredient suppliers before starting full production.



Source:
I leveraged Oreo's core and seasonal consumer review data (across social and review sites) as the foundation for my analysis. Since I do not have access to internal sales or social sentiment databases, I created a realistic synthetic dataset using Python's NumPy library. This approach allowed me to simulate a live database environment, develop an ETL pipeline, and validate my composite scoring model for new product concepts.
