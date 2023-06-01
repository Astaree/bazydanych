

export default class User {
    static entity = 'users'
    
    static fields () {
        return {
        id: this.attr(null),
        name: this.attr(''),
        email: this.attr(''),
        created_at: this.attr(''),
        updated_at: this.attr(''),
        posts: this.hasMany(Post, 'user_id')
        }
    }
    }