import React from 'react';
import axios from 'axios';

const SocialLogin = () => {
    const handleSocialLogin = (provider) => {
        // DjangoバックエンドのソーシャルログインURL
        const backendUrl = `http://localhost:8000/accounts/${provider}/login/`;
        window.location.href = backendUrl;
    };

    return (
        <div>
            <button onClick={() => handleSocialLogin('google')}>Googleでログイン</button>
            <button onClick={() => handleSocialLogin('twitter')}>Twitterでログイン</button>
        </div>
    );
};

export default SocialLogin;