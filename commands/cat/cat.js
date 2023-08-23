const { SlashCommandBuilder } = require("discord.js");
const snoowrap = require("snoowrap");

const reddit = new snoowrap({
    user_agent: "USER_AGENT",
    client_id: "CLIENT_ID",
    client_secret: "CLIENT_SECRET",
    refreshToken: "REFRESH_TOKEN"
})

const subreddits = [
    "OneOrangeBraincell",
    "Catswithjobs",
    "Catloaf",
    "WhatsWrongWithYourCat",
    "teefies",
    "CatsOnKeyboards",
    "blurrypicturesofcats",
]

let data = [];

async function getSubmissions(n) {
    for (const subreddit of subreddits) {
        const hotPosts = await reddit.getHot(subreddit, {limit: n})
        
        hotPosts.forEach((post) => {
            if (post.url.startsWith('https://i')) {
                data.push({
                    link: post.url,
                });
            };
        });
    };
    console.log(`Found ${data.length} submission.`)
    return;
}

async function getRandom() {
    if (data.length === 0){
        await getSubmissions(20);
    }
    const post = data[Math.floor(Math.random() * data.length)];
    const index = data.indexOf(post);
    if (index > -1) {
        data.splice(index, 1)
    };
    return post.link;
}

module.exports = {
    data: new SlashCommandBuilder()
        .setName('cat')
        .setDescription('Replies with a random cat image from reddit.'),
    async execute(interaction) {
        await interaction.deferReply();
        await interaction.editReply(await getRandom());
        
    }
};
