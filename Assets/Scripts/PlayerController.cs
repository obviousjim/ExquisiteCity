using UnityEngine;
using System.Collections;


public class PlayerController : MonoBehaviour {
	public GameObject walkingCameraObject;
	public GameObject flyingCameraObject;

	// Use this for initialization
	void Start () {
		walkingCameraObject.SetActive(true);
		flyingCameraObject.SetActive(false);
	}
	
	// Update is called once per frame
	void Update () {
		if(Input.GetKeyDown(KeyCode.Return)){
			walkingCameraObject.SetActive(!walkingCameraObject.activeSelf);
			flyingCameraObject.SetActive(!flyingCameraObject.activeSelf);
		}
	}
}
