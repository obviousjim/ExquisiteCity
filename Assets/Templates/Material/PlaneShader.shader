
Shader "Custom/PlaneGuideSimple" {
    SubShader {
        Pass {
            Material {
                Diffuse (1,.5,1,1)
                Ambient (1,.5,1,1)
            }
            Lighting On
            Cull Off
        }
    }
	FallBack "Diffuse"
}
