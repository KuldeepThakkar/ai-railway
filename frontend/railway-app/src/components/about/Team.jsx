import React from 'react';

const Team = () => {
    return (
        <section className="w-full max-w-7xl mx-auto px-4 py-20 sm:px-6 lg:px-8">
            <div className="mb-12">
                <h2 className="text-3xl font-bold text-white tracking-tight">Engineers behind the Edge</h2>
                <p className="text-slate-400 mt-2">The minds building the future of autonomous rail inspection.</p>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                {/* Team Member 1 */}
                <div className="group relative rounded-xl bg-surface-dark border border-border-dark overflow-hidden hover:-translate-y-2 transition-transform duration-300">
                    <div className="aspect-[4/5] w-full overflow-hidden bg-slate-800 relative">
                        <img className="h-full w-full object-cover transition-transform duration-500 group-hover:scale-110 opacity-80 group-hover:opacity-100" src="https://lh3.googleusercontent.com/aida-public/AB6AXuA7dsk-OzUOGnGkaA-J74kA6FnGL1TSsv4sV2TVU-SGY6Wsoz1HydR_sIIwBBD0h_k1U4TxkP-cqKYm2NHVCBbjz9GPclQXyq9yc4t6qGiqxhR26bKlTuIfCJkOlCtxuyje-gRPdJ4PsZ-kWndqDavuH8jQwQwlQWhnIsGPuNolnY2ObaW_kyDavBYc48rFOIB3tFuUmXabvGOCgskBRcyAAc7OY2OfMWnd0D6DxyhJk_YWXZEbD5qOj5lhSvKJwGLFpj_EbdKmxL0g" alt="Portrait of Dr. Elena Rostova, Chief Vision Architect" />
                        <div className="absolute inset-0 bg-gradient-to-t from-surface-dark to-transparent opacity-90"></div>
                        <div className="absolute bottom-4 left-4">
                            <p className="text-primary text-xs font-bold uppercase tracking-wider mb-1">Chief Vision Architect</p>
                            <h3 className="text-lg font-bold text-white">Dr. Elena Rostova</h3>
                        </div>
                    </div>
                </div>
                {/* Team Member 2 */}
                <div className="group relative rounded-xl bg-surface-dark border border-border-dark overflow-hidden hover:-translate-y-2 transition-transform duration-300">
                    <div className="aspect-[4/5] w-full overflow-hidden bg-slate-800 relative">
                        <img className="h-full w-full object-cover transition-transform duration-500 group-hover:scale-110 opacity-80 group-hover:opacity-100" src="https://lh3.googleusercontent.com/aida-public/AB6AXuA4I8qeQWWio9WBkKtN1i-PEe4kYeolOs2EgFAsYBWzn_hQQNw_Dbzpp_9ocoz4CvezhWav7fPEaUIPdKgV1JOGjUibIcvMi48C45wQRDSQPeq_nTf0bivWQeAIJJx_0V8qkZHO37cWYlwOCn6TA02DapQngXbCYZZwy-Vrb9tGoxTGYUnz4VumRNVFXrEuUlmZjPcH8_lw5WPTWgOviygbog6vYL3PVW2jY4UC4NZwtAprZDtBqa2AT54JVeJLiJ8AZzTgI2djm-LM" alt="Portrait of Marcus Chen, Lead Systems Engineer" />
                        <div className="absolute inset-0 bg-gradient-to-t from-surface-dark to-transparent opacity-90"></div>
                        <div className="absolute bottom-4 left-4">
                            <p className="text-primary text-xs font-bold uppercase tracking-wider mb-1">Lead Systems Engineer</p>
                            <h3 className="text-lg font-bold text-white">Marcus Chen</h3>
                        </div>
                    </div>
                </div>
                {/* Team Member 3 */}
                <div className="group relative rounded-xl bg-surface-dark border border-border-dark overflow-hidden hover:-translate-y-2 transition-transform duration-300">
                    <div className="aspect-[4/5] w-full overflow-hidden bg-slate-800 relative">
                        <img className="h-full w-full object-cover transition-transform duration-500 group-hover:scale-110 opacity-80 group-hover:opacity-100" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDzlYw9viWaE-zubReBBix47Z1QMFATtVeHMpz4D7R7VIP2mpRHxuyFroxcctqgqbG1DlmchoMXKTb9Zu0HPUoYEtrn4KSSTCVsraNejEOsLtW-K5iMxivb4hohLdmNgfaO2o2SEvOJh3Ulo_aC5MKmTIX8eJGf3bipvzcpryLwK0W9Ff_U1ZO2hBGdQBFq3PjDX54WPyNtexU42q6V4-m-QmoOiXomO__PLlfmdFxXLcwFj0_HAngmeCkeDTvcwyLF143utrbJ194y" alt="Portrait of Sarah Jenkins, Head of AI Research" />
                        <div className="absolute inset-0 bg-gradient-to-t from-surface-dark to-transparent opacity-90"></div>
                        <div className="absolute bottom-4 left-4">
                            <p className="text-primary text-xs font-bold uppercase tracking-wider mb-1">Head of AI Research</p>
                            <h3 className="text-lg font-bold text-white">Sarah Jenkins</h3>
                        </div>
                    </div>
                </div>
                {/* Team Member 4 */}
                <div className="group relative rounded-xl bg-surface-dark border border-border-dark overflow-hidden hover:-translate-y-2 transition-transform duration-300">
                    <div className="aspect-[4/5] w-full overflow-hidden bg-slate-800 relative">
                        <img className="h-full w-full object-cover transition-transform duration-500 group-hover:scale-110 opacity-80 group-hover:opacity-100" src="https://lh3.googleusercontent.com/aida-public/AB6AXuACT76RyTzPumTKL1Ca1jAdyw3NTSPpl--4Vc1ZugyEYzB11J_lwhJU8YS7mI3MnV93NwWQj2AoVVg_0lNbPIG7pHtLO1C5ZyEjDLOOPeOidVfdmtwbsilyB1GYqCAeIvcwKHrmVJP-_vM8txOseofk5vPG9n9Kur4SiVR0YJm-9BzID33IJRq4l-noQoRrfGRNHg6CsMcassM6qV5V9q3wbHFmLEEHvWzXHfxF-jfFbXiJkx7SHvNxkex4YQrHmOYUJZK5CewcL6lW" alt="Portrait of David Okonjo, Operations Director" />
                        <div className="absolute inset-0 bg-gradient-to-t from-surface-dark to-transparent opacity-90"></div>
                        <div className="absolute bottom-4 left-4">
                            <p className="text-primary text-xs font-bold uppercase tracking-wider mb-1">Operations Director</p>
                            <h3 className="text-lg font-bold text-white">David Okonjo</h3>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default Team;
